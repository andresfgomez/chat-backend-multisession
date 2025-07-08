from fastapi import APIRouter
from app.session_manager import SessionManager

router = APIRouter()
session_manager = SessionManager()

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