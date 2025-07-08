from fastapi import FastAPI
from app import api, websocket
from app.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ChatGPT-style Backend",
    description="FastAPI backend with WebSocket and OpenAI integration",
    version="2.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.router, prefix="/api")
app.include_router(websocket.router)