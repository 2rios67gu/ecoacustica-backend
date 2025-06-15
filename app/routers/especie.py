from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.especie import EspecieCreate, EspecieUpdate, EspecieInDB
from app.crud import especie as crud_especie
from typing import List

router = APIRouter(prefix="/especies", tags=["Especies"])

@router.get("/", response_model=List[EspecieInDB])
def listar_especies(db: Session = Depends(get_db)):
    return crud_especie.get_all_especies(db)

@router.get("/{especie_id}", response_model=EspecieInDB)
def obtener_especie(especie_id: int, db: Session = Depends(get_db)):
    especie = crud_especie.get_especie_by_id(db, especie_id)
    if not especie:
        raise HTTPException(status_code=404, detail="Especie no encontrada")
    return especie

@router.post("/", response_model=EspecieInDB)
def crear_especie(especie: EspecieCreate, db: Session = Depends(get_db)):
    return crud_especie.create_especie(db, especie)

@router.put("/{especie_id}", response_model=EspecieInDB)
def actualizar_especie(especie_id: int, especie: EspecieUpdate, db: Session = Depends(get_db)):
    return crud_especie.update_especie(db, especie_id, especie)

@router.delete("/{especie_id}", response_model=EspecieInDB)
def eliminar_especie(especie_id: int, db: Session = Depends(get_db)):
    return crud_especie.delete_especie(db, especie_id)
