# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code and scripts
COPY app/ ./app/
COPY mini_games/ ./mini_games/
COPY questions_data/ ./questions_data/
COPY recreate_db.py .
COPY seed_questions.py .
COPY generate_haunting_questions.py .
COPY load_haunting_race_questions.py .
COPY .env .env.example ./

# Copy startup script
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Expose port
EXPOSE 8000

# Use startup script as entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]