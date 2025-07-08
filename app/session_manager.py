from sqlalchemy.orm import Session as DBSession
from app.db import SessionLocal
from app.models import Session, Message

class SessionManager:
    def __init__(self):
        self.db: DBSession = SessionLocal()

    def create_session(self, session_id: str):
        session = self.db.query(Session).filter_by(session_id=session_id).first()
        if not session:
            session = Session(session_id=session_id)
            self.db.add(session)
            self.db.commit()

    def add_message(self, session_id: str, role: str, content: str):
        session = self.db.query(Session).filter_by(session_id=session_id).first()
        if session:
            message = Message(session=session, role=role, content=content)
            self.db.add(message)
            self.db.commit()

    def get_session_messages(self, session_id: str):
        session = self.db.query(Session).filter_by(session_id=session_id).first()
        if session:
            return [{"role": msg.role, "content": msg.content} for msg in session.messages]
        return []

    def list_sessions(self):
        return self.db.query(Session).all()

    def remove_session(self, session_id: str):
        session = self.db.query(Session).filter_by(session_id=session_id).first()
        if session:
            self.db.delete(session)
            self.db.commit()