from fastapi import APIRouter
from app.session_manager import SessionManager
from app.db import SessionLocal
from app.models import Session
import uuid

router = APIRouter()
session_manager = SessionManager()


@router.post("/sessions")
def create_session():
    db = SessionLocal()
    session_id = str(uuid.uuid4())
    new_session = Session(session_id=session_id)
    db.add(new_session)
    db.commit()
    db.close()
    return {"session_id": session_id, "created_at": new_session.created_at}

@router.get("/sessions")
def list_sessions():
    sessions = session_manager.list_sessions()
    return [{"session_id": s.session_id, "created_at": s.created_at} for s in sessions]

@router.get("/sessions/{session_id}/history")
def get_chat_history(session_id: str):
    return {
        "session_id": session_id,
        "messages": session_manager.get_session_messages(session_id)
    }