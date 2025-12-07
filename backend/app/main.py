from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from dotenv import load_dotenv

from app.routes import rooms, game
from app.websockets.manager import connection_manager
from app.models.database import engine, Base
from app.services.game_service import GameService

# Load environment variables
load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Knockout Trivia API",
    description="Backend API for multiplayer trivia game",
    version="1.0.0"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services (using singleton connection_manager from manager module)
game_service = GameService(connection_manager)

# Make connection_manager available to routers
app.state.connection_manager = connection_manager
app.state.game_service = game_service

# Include routers
app.include_router(rooms.router, prefix="/api/rooms", tags=["rooms"])
app.include_router(game.router, prefix="/api/game", tags=["game"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "knockout-trivia-api"}

@app.get("/api/leaderboard")
async def get_global_leaderboard():
    from app.models.database import get_db
    from app.models.models import HighScore

    db = next(get_db())
    try:
        # Get top 5 high scores across all completed games
        high_scores = db.query(HighScore).order_by(
            HighScore.score.desc()
        ).limit(5).all()

        return [
            {
                "name": high_score.player_name,
                "score": high_score.score,
                "rank": idx + 1,
                "questions_answered": high_score.questions_answered,
                "correct_answers": high_score.correct_answers,
                "achieved_at": high_score.achieved_at.isoformat() if high_score.achieved_at else None
            }
            for idx, high_score in enumerate(high_scores)
        ]
    finally:
        db.close()

@app.delete("/api/leaderboard")
async def reset_leaderboard():
    """Delete all high scores from the leaderboard"""
    from app.models.database import get_db
    from app.models.models import HighScore

    db = next(get_db())
    try:
        # Delete all high scores
        deleted_count = db.query(HighScore).delete()
        db.commit()

        return {
            "message": "Leaderboard reset successfully",
            "deleted_count": deleted_count
        }
    finally:
        db.close()

@app.websocket("/ws/{room_code}/{player_id}")
async def websocket_endpoint(websocket: WebSocket, room_code: str, player_id: str):
    await connection_manager.connect(websocket, room_code, player_id)
    try:
        while True:
            data = await websocket.receive_text()
            await game_service.handle_websocket_message(room_code, player_id, data)
    except WebSocketDisconnect:
        await connection_manager.disconnect(room_code, player_id)
        await game_service.handle_player_disconnect(room_code, player_id)

# Serve frontend static files (for production deployment)
# This should be after all API routes to avoid conflicts
# Try multiple possible paths for frontend
possible_frontend_paths = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "frontend"),  # Local dev
    os.path.join(os.getcwd(), "frontend"),  # Railway deployment
    os.path.join(os.path.dirname(os.getcwd()), "frontend"),  # Alternative
]

frontend_path = None
for path in possible_frontend_paths:
    abs_path = os.path.abspath(path)
    if os.path.exists(abs_path):
        frontend_path = abs_path
        break

if frontend_path and os.path.exists(frontend_path):
    print(f"[INFO] Serving frontend from: {frontend_path}")
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    print(f"[WARNING] Frontend path not found. Tried paths:")
    for path in possible_frontend_paths:
        print(f"  - {os.path.abspath(path)} (exists: {os.path.exists(os.path.abspath(path))})")
    print(f"[WARNING] Current working directory: {os.getcwd()}")

if __name__ == "__main__":
    # Get port from environment variable (Railway sets this)
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )