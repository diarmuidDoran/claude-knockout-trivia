from fastapi import WebSocket
from typing import Dict, List
import json
import asyncio
from datetime import datetime

class ConnectionManager:
    def __init__(self):
        # Structure: {room_code: {player_id: websocket}}
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {}
        
    async def connect(self, websocket: WebSocket, room_code: str, player_id: str):
        await websocket.accept()
        
        if room_code not in self.active_connections:
            self.active_connections[room_code] = {}
            
        self.active_connections[room_code][player_id] = websocket
        
        # Notify other players in the room
        await self.broadcast_to_room(
            room_code, 
            {
                "type": "player_joined",
                "player_id": player_id,
                "timestamp": datetime.utcnow().isoformat()
            },
            exclude_player=player_id
        )
    
    async def disconnect(self, room_code: str, player_id: str):
        if room_code in self.active_connections:
            if player_id in self.active_connections[room_code]:
                del self.active_connections[room_code][player_id]
                
                # Notify other players
                await self.broadcast_to_room(
                    room_code,
                    {
                        "type": "player_left",
                        "player_id": player_id,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )

                # Clean up empty rooms
                if room_code in self.active_connections and not self.active_connections[room_code]:
                    del self.active_connections[room_code]
    
    async def send_personal_message(self, message: dict, room_code: str, player_id: str):
        if room_code in self.active_connections:
            if player_id in self.active_connections[room_code]:
                websocket = self.active_connections[room_code][player_id]
                try:
                    await websocket.send_text(json.dumps(message))
                except:
                    # Connection is broken, clean it up
                    await self.disconnect(room_code, player_id)
    
    async def broadcast_to_room(self, room_code: str, message: dict, exclude_player: str = None):
        if room_code not in self.active_connections:
            return

        message_str = json.dumps(message)
        disconnected_players = []

        # Create a copy of the dict items to avoid "dictionary changed size during iteration"
        connections_snapshot = list(self.active_connections[room_code].items())

        for player_id, websocket in connections_snapshot:
            if exclude_player and player_id == exclude_player:
                continue

            try:
                await websocket.send_text(message_str)
            except:
                # Connection is broken, mark for cleanup
                disconnected_players.append(player_id)

        # Clean up broken connections
        for player_id in disconnected_players:
            await self.disconnect(room_code, player_id)
    
    def get_room_players(self, room_code: str) -> List[str]:
        if room_code in self.active_connections:
            return list(self.active_connections[room_code].keys())
        return []
    
    def get_player_count(self, room_code: str) -> int:
        if room_code in self.active_connections:
            return len(self.active_connections[room_code])
        return 0

    # Haunting Race WebSocket Events
    async def broadcast_haunting_race_start(self, room_code: str, race_data: dict):
        """Broadcast haunting race start to all players in room."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_start",
            "data": race_data,
            "timestamp": datetime.utcnow().isoformat()
        })

    async def broadcast_haunting_race_question(self, room_code: str, question_data: dict):
        """Broadcast haunting race question to all players."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_question",
            "data": question_data,
            "timestamp": datetime.utcnow().isoformat()
        })

    async def send_haunting_race_player_question(self, room_code: str, player_id: str, question_data: dict, is_unicorn: bool):
        """Send question with appropriate statements (unicorn sees 2, ghosts see 3)."""
        # Filter statements based on player role
        filtered_statements = []
        for stmt in question_data["statements"]:
            if is_unicorn and stmt.get("is_ghost_only", False):
                continue  # Unicorn doesn't see ghost-only statements
            filtered_statements.append(stmt)

        player_question_data = {**question_data, "statements": filtered_statements}

        await self.send_personal_message({
            "type": "haunting_race_question",
            "data": player_question_data,
            "is_unicorn": is_unicorn,
            "timestamp": datetime.utcnow().isoformat()
        }, room_code, str(player_id))

    async def broadcast_haunting_race_positions(self, room_code: str, positions: dict, movements: dict = None):
        """Broadcast updated positions after a question."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_positions",
            "positions": positions,
            "movements": movements or {},
            "timestamp": datetime.utcnow().isoformat()
        })

    async def broadcast_haunting_race_unicorn_swap(self, room_code: str, swap_data: dict):
        """Broadcast unicorn swap event (ghost caught unicorn)."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_unicorn_swap",
            "swap_data": swap_data,
            "timestamp": datetime.utcnow().isoformat()
        })

    async def broadcast_haunting_race_results(self, room_code: str, results: dict):
        """Broadcast question results."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_results",
            "results": results,
            "timestamp": datetime.utcnow().isoformat()
        })

    async def broadcast_haunting_race_end(self, room_code: str, winner_data: dict):
        """Broadcast haunting race end with winner."""
        await self.broadcast_to_room(room_code, {
            "type": "haunting_race_end",
            "data": winner_data,
            "timestamp": datetime.utcnow().isoformat()
        })


# Singleton instance
connection_manager = ConnectionManager()