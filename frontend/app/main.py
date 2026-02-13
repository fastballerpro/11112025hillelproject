from fastapi import FastAPI

def get_application() -> FastAPI:
    _app = FastAPI(
        debug=True
    )
    return _app

app = get_application()