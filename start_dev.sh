#!/usr/bin/env bash
set -e

# Start FastAPI backend
uvicorn backend.main:app --reload &
BACK_PID=$!

# Ensure backend process is terminated on script exit
trap "kill $BACK_PID" EXIT

# Start simple HTTP server for frontend
cd frontend
python3 -m http.server 3000
