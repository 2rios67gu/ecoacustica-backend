from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.models.audio import Audio
from app.schemas.audio import AudioCreate

def get_all(db: Session):
    return db.query(Audio).all()

def get_by_id(db: Session, audio_id: int):
    return db.query(Audio).filter(Audio.aud_int_id == audio_id).first()

def create(db: Session, audio: AudioCreate):
    db_audio = Audio(**audio.dict())
    db.add(db_audio)
    db.commit()
    db.refresh(db_audio)
    return db_audio

def delete(db: Session, audio_id: int):
    db_audio = get_by_id(db, audio_id)
    if db_audio:
        db.delete(db_audio)
        db.commit()
    return db_audio
