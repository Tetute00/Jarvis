#!/bin/bash
# Script to run the FastAPI server

# Navigate to the server directory (adjust path if needed)
cd "$(dirname "$0")/../" || exit

# Activate virtual environment if you use one
# source ../.venv/bin/activate

echo "Starting Jarvis Server..."
# Use uvicorn directly or python main.py depending on your preference
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
python app/main.py