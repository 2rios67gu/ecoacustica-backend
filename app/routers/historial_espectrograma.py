from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.historial_espectrograma import HistorialEspectrograma, HistorialEspectrogramaCreate
from app.crud import historial_espectrograma as crud
from app.database.session import get_db

router = APIRouter(prefix="/historial", tags=["Historial Espectrograma"])

@router.get("/", response_model=List[HistorialEspectrograma])
def listar_historial(db: Session = Depends(get_db)):
    return crud.get_all_historial(db)

@router.get("/{historial_id}", response_model=HistorialEspectrograma)
def obtener_historial(historial_id: int, db: Session = Depends(get_db)):
    db_historial = crud.get_historial_by_id(db, historial_id)
    if not db_historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return db_historial

@router.post("/", response_model=HistorialEspectrograma)
def crear_historial(historial: HistorialEspectrogramaCreate, db: Session = Depends(get_db)):
    return crud.create_historial(db, historial)

@router.delete("/{historial_id}", response_model=HistorialEspectrograma)
def eliminar_historial(historial_id: int, db: Session = Depends(get_db)):
    db_historial = crud.delete_historial(db, historial_id)
    if not db_historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return db_historial
