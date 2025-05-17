from sqlalchemy import Column, Integer, String
from .database import Base

class Flashcard(Base):
    __tablename__ = "flashcards"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    question = Column(String)
    answer = Column(String)
    subject = Column(String)