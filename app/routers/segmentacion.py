from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.segmentacion import SegmentacionCreate, SegmentacionOut
from app.crud import segmentacion as crud_segmentacion
from app.database.session import get_db

router = APIRouter(prefix="/segmentaciones", tags=["Segmentaciones"])

@router.post("/", response_model=SegmentacionOut)
def create_segmentacion(segmentacion: SegmentacionCreate, db: Session = Depends(get_db)):
    return crud_segmentacion.create_segmentacion(db, segmentacion)

@router.get("/", response_model=List[SegmentacionOut])
def read_segmentaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_segmentacion.get_segmentaciones(db, skip, limit)

@router.get("/{seg_int_id}", response_model=SegmentacionOut)
def read_segmentacion(seg_int_id: int, db: Session = Depends(get_db)):
    db_obj = crud_segmentacion.get_segmentacion(db, seg_int_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Segmentación no encontrada")
    return db_obj
