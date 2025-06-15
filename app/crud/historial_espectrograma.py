from sqlalchemy.orm import Session
from app.models.historial_espectrograma import HistorialEspectrograma
from app.schemas.historial_espectrograma import HistorialEspectrogramaCreate

def get_all_historial(db: Session):
    return db.query(HistorialEspectrograma).all()

def get_historial_by_id(db: Session, historial_id: int):
    return db.query(HistorialEspectrograma).filter(HistorialEspectrograma.his_int_id == historial_id).first()

def create_historial(db: Session, historial: HistorialEspectrogramaCreate):
    db_historial = HistorialEspectrograma(**historial.dict())
    db.add(db_historial)
    db.commit()
    db.refresh(db_historial)
    return db_historial

def delete_historial(db: Session, historial_id: int):
    db_historial = get_historial_by_id(db, historial_id)
    if db_historial:
        db.delete(db_historial)
        db.commit()
    return db_historial
