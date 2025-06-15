from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.resultado_identificacion import ResultadoIdentificacion, ResultadoIdentificacionCreate
from app.crud import resultado_identificacion as crud
from app.database.session import get_db

router = APIRouter(prefix="/resultados", tags=["Resultado de Identificación"])

@router.get("/", response_model=List[ResultadoIdentificacion])
def listar_resultados(db: Session = Depends(get_db)):
    return crud.get_all_resultados(db)

@router.get("/{resultado_id}", response_model=ResultadoIdentificacion)
def obtener_resultado(resultado_id: int, db: Session = Depends(get_db)):
    db_resultado = crud.get_resultado_by_id(db, resultado_id)
    if not db_resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return db_resultado

@router.post("/", response_model=ResultadoIdentificacion)
def crear_resultado(resultado: ResultadoIdentificacionCreate, db: Session = Depends(get_db)):
    return crud.create_resultado(db, resultado)

@router.delete("/{resultado_id}", response_model=ResultadoIdentificacion)
def eliminar_resultado(resultado_id: int, db: Session = Depends(get_db)):
    db_resultado = crud.delete_resultado(db, resultado_id)
    if not db_resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return db_resultado
