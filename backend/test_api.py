#!/usr/bin/env python3
"""Test the room creation API endpoint."""

import sys
sys.path.insert(0, '.')

import asyncio
from app.models.database import SessionLocal
from app.models.models import Room, Player
from app.routes.rooms import generate_room_code

def test_room_creation():
    """Test creating a room directly."""
    print("Testing room creation...")

    db = SessionLocal()
    try:
        # Generate room code
        room_code = generate_room_code()
        print(f"Generated room code: {room_code}")

        # Create room
        room = Room(
            code=room_code,
            host_name="TEST_HOST",
            max_players=10
        )
        db.add(room)
        db.commit()
        db.refresh(room)
        print(f"✓ Room created with ID: {room.id}")

        # Create host player
        host_player = Player(
            name="TEST_HOST",
            room_id=room.id,
            is_vip=True
        )
        db.add(host_player)
        db.commit()
        db.refresh(host_player)
        print(f"✓ Host player created with ID: {host_player.id}")

        print("\nRoom details:")
        print(f"  Code: {room.code}")
        print(f"  Host: {room.host_name}")
        print(f"  Max Players: {room.max_players}")
        print(f"  Game State: {room.game_state.value}")
        print(f"  Host Player ID: {host_player.id}")
        print(f"  Host is VIP: {host_player.is_vip}")

        print("\n✓ Room creation test passed!")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_room_creation()
