# 11112025hillelproject
# Windows:
/backend     uv init
/backend     uv add fastapi[standard]
/backend/app           uv run -m uvicorn main:app --reload

# MacOS:
/backend     uv init
/backend     uv add "fastapi[standard]"
/backend/app           uv run -m uvicorn main:app --reload
