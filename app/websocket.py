from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.openai_utils import stream_openai_response
from app.session_manager import SessionManager
import uuid

router = APIRouter()
session_manager = SessionManager()

@router.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket):
    await websocket.accept()
    session_id = str(uuid.uuid4())
    session_manager.create_session(session_id)
    await websocket.send_json({"session_id": session_id})
    
    try:
        while True:
            data = await websocket.receive_json()
            user_message = data.get("message")
            print(f"[{session_id}] User: {user_message}")
            session_manager.add_message(session_id, "user", user_message)

            for response_chunk in stream_openai_response(session_manager.get_session_messages(session_id)):
                await websocket.send_json({"response": response_chunk})
            session_manager.add_message(session_id, "assistant", response_chunk)
    except WebSocketDisconnect:
        print(f"[{session_id}] Disconnected")
        session_manager.remove_session(session_id)