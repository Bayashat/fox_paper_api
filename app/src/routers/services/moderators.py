from sqlalchemy.orm import Session

from ...models.research import Research


def get_pending_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "PENDING").all()
    if not reserches:
        return {"message": "No pending researches found"}
    return reserches


def get_published_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "PUBLISHED").all()
    if not reserches:
        return {"message": "No published researches found"}
    return reserches


def get_rejected_researches(db: Session):
    reserches = db.query(Research).filter(Research.status == "REJECTED").all()
    if not reserches:
        return {"message": "No rejected researches found"}
    return reserches


def delete_research(db: Session, research_id: int):
    research = db.query(Research).filter(Research.id == research_id).first()
    if not research:
        return {"message": "Research not found"}
    db.delete(research)
    db.commit()
    return {"message": "Research deleted"}