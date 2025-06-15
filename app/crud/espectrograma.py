from sqlalchemy.orm import Session
from app.models.espectrograma import Espectrograma
from app.schemas.espectrograma import EspectrogramaCreate

def create_espectrograma(db: Session, espectrograma: EspectrogramaCreate):
    db_obj = Espectrograma(**espectrograma.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_espectrograma(db: Session, esp_int_id: int):
    return db.query(Espectrograma).filter(Espectrograma.esp_int_id == esp_int_id).first()

def get_espectrogramas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Espectrograma).offset(skip).limit(limit).all()
