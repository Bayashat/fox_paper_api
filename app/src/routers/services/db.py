from sqlalchemy.orm import Session

def add_commit_refresh(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
