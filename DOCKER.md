# Knockout Trivia - Docker Deployment

This guide explains how to run the entire Knockout Trivia application using Docker Compose.

## Prerequisites

- Docker Desktop installed (includes Docker and Docker Compose)
- No other services running on ports 3000, 5432, 6379, or 8000

## Quick Start

### 1. Stop Any Existing Services

If you have PostgreSQL running locally:

```bash
# Stop Homebrew PostgreSQL (macOS)
brew services stop postgresql@15

# Or stop any manually running PostgreSQL
# Check what's running on port 5432
lsof -i :5432
```

### 2. Start the Application

From the project root directory:

```bash
# Build and start all services
docker compose up --build

# Or run in detached mode (background)
docker compose up --build -d
```

This single command will:
1. Build the backend Docker image
2. Start PostgreSQL database
3. Start Redis cache
4. Initialize the database schema
5. Generate and load 490 haunting race questions
6. Start the FastAPI backend
7. Start the Nginx frontend server

### 3. Access the Application

Once all services are running:

- **Frontend (Player)**: http://localhost:3000/index.html
- **Frontend (TV Display)**: http://localhost:3000/tv.html
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Managing the Application

### View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f postgres
```

### Stop the Application

```bash
# Stop all services
docker compose down

# Stop and remove volumes (deletes database data)
docker compose down -v
```

### Restart a Specific Service

```bash
# Restart backend
docker compose restart backend

# Restart frontend
docker compose restart frontend
```

### Rebuild After Code Changes

```bash
# Rebuild and restart
docker compose up --build

# Or rebuild specific service
docker compose build backend
docker compose up -d backend
```

## Services

The Docker Compose setup includes 4 services:

### 1. PostgreSQL Database (`postgres`)
- **Port**: 5432
- **Database**: knockout_trivia
- **User**: postgres
- **Password**: password
- **Data**: Persisted in `postgres_data` volume

### 2. Redis Cache (`redis`)
- **Port**: 6379
- **Purpose**: Session management and real-time features

### 3. Backend API (`backend`)
- **Port**: 8000
- **Framework**: FastAPI
- **Auto-initialization**: Creates tables and loads questions on first run
- **Hot reload**: Enabled for development

### 4. Frontend (`frontend`)
- **Port**: 3000
- **Server**: Nginx
- **Proxies**: API calls to backend, WebSocket connections

## Database Initialization

The backend automatically initializes the database on first run:

1. Waits for PostgreSQL to be ready
2. Checks if database is initialized
3. If not initialized:
   - Creates all database tables
   - Generates haunting race questions
   - Loads questions into database
4. Starts the FastAPI server

## Development Workflow

### Live Code Editing

The backend and frontend volumes are mounted for live editing:

- **Frontend**: Edit files in `frontend/` - changes are immediately visible
- **Backend**: Edit files in `backend/app/` - auto-reload is enabled

### Database Access

Connect to PostgreSQL from your local machine:

```bash
# Using psql
psql -h localhost -p 5432 -U postgres -d knockout_trivia
# Password: password

# Or using Docker exec
docker exec -it knockout-trivia-db psql -U postgres -d knockout_trivia
```

### Reset Database

```bash
# Stop services and remove volumes
docker compose down -v

# Start services (will reinitialize database)
docker compose up --build
```

## Troubleshooting

### Port Already in Use

If you get port conflict errors:

```bash
# Check what's using the port
lsof -i :3000
lsof -i :5432
lsof -i :8000

# Stop the conflicting service or change the port in docker-compose.yml
```

### Backend Won't Start

```bash
# Check backend logs
docker compose logs backend

# Restart backend
docker compose restart backend

# Rebuild backend
docker compose build backend
docker compose up -d backend
```

### Database Connection Issues

```bash
# Check PostgreSQL is healthy
docker compose ps

# View PostgreSQL logs
docker compose logs postgres

# Verify database exists
docker exec -it knockout-trivia-db psql -U postgres -l
```

### Questions Not Loading

The backend automatically loads questions on first run. If questions are missing:

```bash
# Access backend container
docker exec -it knockout-trivia-api bash

# Generate questions
python3 generate_haunting_questions.py

# Load questions
python3 load_haunting_race_questions.py
```

## Production Deployment

For production deployment, update the following in `docker-compose.yml`:

1. **Change Passwords**: Update PostgreSQL and other service passwords
2. **Update SECRET_KEY**: Set a secure random key
3. **Set DEBUG=False**: Disable debug mode
4. **Add SSL/TLS**: Configure HTTPS in nginx
5. **Resource Limits**: Add memory and CPU limits
6. **Logging**: Configure proper log aggregation
7. **Backups**: Set up database backup strategy

## Network Architecture

All services communicate via the `trivia-network` Docker network:

```
                    ┌─────────────┐
                    │   Browser   │
                    └─────┬───────┘
                          │ Port 3000
                    ┌─────▼─────────┐
                    │    Nginx      │
                    │  (Frontend)   │
                    └─────┬─────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Port 8000         WebSocket          Port 8000
        │                 │                 │
   ┌────▼────────────────▼──────────────┐  │
   │       FastAPI Backend              │  │
   │    (knockout-trivia-api)           │  │
   └────┬─────────────────────┬─────────┘  │
        │                     │             │
   Port 5432            Port 6379          │
        │                     │             │
   ┌────▼──────┐        ┌────▼─────┐       │
   │PostgreSQL │        │  Redis   │       │
   └───────────┘        └──────────┘       │
                                            │
                                       Data Volume
```

## File Structure

```
knockout-trivia/
├── docker-compose.yml          # Docker Compose configuration
├── backend/
│   ├── Dockerfile              # Backend Docker image
│   ├── docker-entrypoint.sh    # Startup script
│   ├── .dockerignore          # Docker ignore patterns
│   ├── requirements.txt        # Python dependencies
│   ├── recreate_db.py         # Database schema creation
│   ├── generate_haunting_questions.py
│   ├── load_haunting_race_questions.py
│   └── app/                    # FastAPI application
├── frontend/
│   ├── nginx.conf             # Nginx configuration
│   ├── index.html             # Player interface
│   └── tv.html                # TV display
└── DOCKER.md                  # This file
```

## Support

For issues or questions:
- Check the logs: `docker compose logs -f`
- Restart services: `docker compose restart`
- Reset everything: `docker compose down -v && docker compose up --build`
