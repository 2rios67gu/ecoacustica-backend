from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.espectrograma import EspectrogramaCreate, EspectrogramaOut
from app.crud import espectrograma as crud_espectrograma
from app.database.session import get_db

router = APIRouter(prefix="/espectrogramas", tags=["Espectrogramas"])

@router.post("/", response_model=EspectrogramaOut)
def create_espectrograma(espectrograma: EspectrogramaCreate, db: Session = Depends(get_db)):
    return crud_espectrograma.create_espectrograma(db, espectrograma)

@router.get("/", response_model=List[EspectrogramaOut])
def read_espectrogramas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_espectrograma.get_espectrogramas(db, skip, limit)

@router.get("/{esp_int_id}", response_model=EspectrogramaOut)
def read_espectrograma(esp_int_id: int, db: Session = Depends(get_db)):
    db_obj = crud_espectrograma.get_espectrograma(db, esp_int_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Espectrograma no encontrado")
    return db_obj
