from sqlalchemy.orm import Session
from app.models.segmentacion import Segmentacion
from app.schemas.segmentacion import SegmentacionCreate

def create_segmentacion(db: Session, segmentacion: SegmentacionCreate):
    db_obj = Segmentacion(**segmentacion.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_segmentacion(db: Session, seg_int_id: int):
    return db.query(Segmentacion).filter(Segmentacion.seg_int_id == seg_int_id).first()

def get_segmentaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Segmentacion).offset(skip).limit(limit).all()
