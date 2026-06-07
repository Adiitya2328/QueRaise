from fastapi import FastAPI

from backend.routes.query_routes import router as query_router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "QueRaise API is running"
    }


app.include_router(query_router)