from fastapi import FastAPI, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from random import shuffle

from .database import Base, engine, SessionLocal
from .models import Flashcard
from .subject_classifier import infer_subject

app = FastAPI()
Base.metadata.create_all(bind=engine)

class FlashcardIn(BaseModel):
    student_id: str
    question: str
    answer: str

@app.post("/flashcard")
def add_flashcard(flashcard: FlashcardIn):
    db: Session = SessionLocal()
    subject = infer_subject(flashcard.question)

    new_card = Flashcard(
        student_id=flashcard.student_id,
        question=flashcard.question,
        answer=flashcard.answer,
        subject=subject
    )
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    db.close()

    return {"message": "Flashcard added successfully", "subject": subject}

@app.get("/get-subject")
def get_flashcards(student_id: str = Query(...), limit: int = Query(5)):
    db: Session = SessionLocal()
    all_cards = db.query(Flashcard).filter(Flashcard.student_id == student_id).all()
    db.close()

    subject_map = {}
    for card in all_cards:
        subject_map.setdefault(card.subject, []).append(card)

    result = []
    for cards in subject_map.values():
        shuffle(cards)
        result.extend(cards[:1])

    shuffle(result)
    return [
        {
            "question": card.question,
            "answer": card.answer,
            "subject": card.subject
        }
        for card in result[:limit]
    ]