# 11112025hillelproject
# Windows:
/backend     uv init
/backend     uv add fastapi[standard]
/backend/app           uv run -m uvicorn main:app --reload
docker compose up  --build

# MacOS:
/backend     uv init
/backend     uv add "fastapi[standard]"
/backend/app           uv run -m uvicorn main:app --reload
docker compose up  --build
