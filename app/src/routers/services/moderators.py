from sqlalchemy.orm import Session
from fastapi import HTTPException

from ...models.research import Research


def get_pending_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "SUBMITTED").all()
    print(reserches)
    if not reserches:
        raise HTTPException(status_code=404, detail="No pending researches found")
    return reserches


def get_published_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "PUBLISHED").all()
    if not reserches:
        raise HTTPException(status_code=404, detail="No published researches found")
    return reserches


def get_rejected_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "REJECTED").all()
    if not reserches:
        raise HTTPException(status_code=404, detail="No rejected researches found")
    return reserches


def delete_research(db: Session, research_id: int):
    research = db.query(Research).filter(Research.id == research_id).first()
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    db.delete(research)
    db.commit()
    return {"message": "Research deleted"}