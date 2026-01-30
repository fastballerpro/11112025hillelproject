# Simple Market FastAPI App

## Run locally

```bash
cd /backend
uv init
uv add "fastapi[standard]"
uv add passlib
uv add bcrypt==4.1.3
cd /backend/app
uv run -m uvicorn main:app --reload
# if you want run in docker
docker compose up

# Docker Build
docker compose up --build
And you're good to go 🚀