# Claude Code Guidelines for Knockout Trivia

## Project Architecture

This project is a real-time multiplayer trivia game with the following technology stack:

### Backend

- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Real-time Communication**: WebSockets
- **ORM**: SQLAlchemy

### Frontend

- **Language**: JavaScript (Vanilla JS)
- **Real-time**: WebSocket connections
- **Architecture**: Separate apps for TV display and mobile players

### Deployment

- **Containerization**: Docker containers
- **Database**: PostgreSQL container

## Coding Standards

### Python/FastAPI Backend

1. **Always use FastAPI** for API endpoints

   - Use async/await for all route handlers
   - Leverage Pydantic models for request/response validation
   - Use dependency injection for database sessions
2. **Database**

   - Use PostgreSQL for production
   - SQLite is acceptable for local development only
   - Always use SQLAlchemy ORM
   - Define proper relationships between models
   - Use migrations (Alembic) for schema changes
3. **WebSocket Communication**

   - Implement WebSocket endpoints using FastAPI's WebSocket support
   - Use ConnectionManager pattern for managing active connections
   - Broadcast events to rooms for multiplayer synchronization
4. **Code Organization**

   ```
   backend/
   ├── app/
   │   ├── main.py              # FastAPI app initialization
   │   ├── models/
   │   │   ├── database.py      # Database connection
   │   │   └── models.py        # SQLAlchemy models
   │   ├── routes/              # API endpoints
   │   ├── services/            # Business logic
   │   └── websockets/          # WebSocket managers
   ```

### Frontend JavaScript

1. **Use Vanilla JavaScript**

   - No frameworks (React, Vue, etc.)
   - ES6+ features are encouraged
   - Class-based architecture for managers
2. **WebSocket Integration**

   - Use native WebSocket API
   - Implement reconnection logic
   - Handle all real-time events via WebSocket
3. **Code Organization**

   ```
   frontend/
   ├── index.html           # Mobile player interface
   ├── tv.html              # TV/laptop display
   ├── js/
   │   ├── config.js        # Configuration
   │   ├── websocket.js     # WebSocket manager
   │   ├── mobile-app.js    # Mobile player logic
   │   └── tv-app.js        # TV display logic
   └── css/                 # Styles
   ```

### Docker Deployment

1. **Container Requirements**

   - Create Dockerfile for FastAPI backend
   - Use docker-compose.yml for multi-container setup
   - Include PostgreSQL service
   - Frontend served via nginx or similar
2. **Environment Variables**

   - Use .env files for configuration
   - Never commit secrets to version control
   - Document all required environment variables

## Development Guidelines

### When Adding Features

1. **Backend Changes**

   - Create API endpoint in appropriate routes file
   - Add database models if needed
   - Implement WebSocket broadcasting for real-time updates
   - Update ConnectionManager if needed
2. **Frontend Changes**

   - Update WebSocketManager event handlers
   - Add UI elements to HTML
   - Implement corresponding CSS styles
   - Update config.js if new settings needed
3. **Database Changes**

   - Create Alembic migration
   - Update SQLAlchemy models
   - Test migration up/down

### Real-time Communication Pattern

1. **Player Actions** → API Endpoint → Database Update → WebSocket Broadcast
2. **All clients** receive updates via WebSocket
3. **UI Updates** happen in response to WebSocket events

### API Design Principles

- RESTful endpoints for CRUD operations
- WebSocket for real-time bidirectional communication
- Pydantic models for request/response validation
- Proper HTTP status codes and error messages

## Current Implementation Notes

### Database

- Currently using SQLite for local development
- Switch to PostgreSQL for production via DATABASE_URL environment variable
- Connection string format: `postgresql://user:password@host:port/database`

### Ports

- Backend API: Port 8000 (default) or 8001
- Frontend: Port 3000 (when using development server)
- PostgreSQL: Port 5432 (default)

### WebSocket Flow

1. **Room Creation**

   - POST /api/rooms/create → Returns room_code and host_player_id
   - TV app connects to WebSocket: ws://host/ws/{room_code}/{player_id}
2. **Player Joining**

   - POST /api/rooms/join → Returns player info
   - Mobile app connects to WebSocket
   - Server broadcasts "player_joined" event to all in room
3. **Game Start**

   - POST /api/game/start (VIP player only)
   - Server broadcasts "game_started" event
   - Game service starts question flow

## Commands Reference

### Development

```bash
# Backend
cd backend
python3 -m uvicorn app.main:app --reload --port 8001

# Frontend (simple HTTP server)
cd frontend
python3 -m http.server 3000
```

### Docker (Future)

```bash
# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

## Important Reminders for Claude

1. ✅ Always use FastAPI, never Flask or Django
2. ✅ Always use PostgreSQL for production
3. ✅ Always use WebSockets for real-time features
4. ✅ Always use Vanilla JavaScript, no frameworks
5. ✅ Always consider Docker deployment when making architectural decisions
6. ✅ Always broadcast WebSocket events when state changes affect multiple clients
7. ✅ Always validate requests with Pydantic models
8. ✅ Always use async/await in FastAPI routes
9. ✅ Never commit .env files or secrets
10. ✅ Always update both API and WebSocket when adding features

## Testing Locally

1. Start backend: `python3 -m uvicorn app.main:app --reload --port 8001`
2. Start frontend: `python3 -m http.server 3000` (from frontend directory)
3. Open TV: `http://localhost:3000/tv.html`
4. Open mobile: `http://localhost:3000/index.html`
5. Test multiplayer with multiple browser tabs

---

**Last Updated**: 2025-11-14
