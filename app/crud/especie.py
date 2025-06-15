from sqlalchemy.orm import Session
from app.models.especie import Especie
from app.schemas.especie import EspecieCreate, EspecieUpdate

def get_all_especies(db: Session):
    return db.query(Especie).all()

def get_especie_by_id(db: Session, especie_id: int):
    return db.query(Especie).filter(Especie.esp_int_id == especie_id).first()

def create_especie(db: Session, especie: EspecieCreate):
    db_especie = Especie(**especie.dict())
    db.add(db_especie)
    db.commit()
    db.refresh(db_especie)
    return db_especie

def update_especie(db: Session, especie_id: int, especie: EspecieUpdate):
    db_especie = get_especie_by_id(db, especie_id)
    if db_especie:
        for field, value in especie.dict().items():
            setattr(db_especie, field, value)
        db.commit()
        db.refresh(db_especie)
    return db_especie

def delete_especie(db: Session, especie_id: int):
    db_especie = get_especie_by_id(db, especie_id)
    if db_especie:
        db.delete(db_especie)
        db.commit()
    return db_especie
