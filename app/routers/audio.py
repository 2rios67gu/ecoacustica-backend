from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas import audio as schemas
from app.crud import audio as crud

router = APIRouter(prefix="/audios", tags=["Audios"])

@router.get("/", response_model=list[schemas.Audio])
def listar_audios(db: Session = Depends(get_db)):
    return crud.get_all(db)

@router.get("/{audio_id}", response_model=schemas.Audio)
def obtener_audio(audio_id: int, db: Session = Depends(get_db)):
    db_audio = crud.get_by_id(db, audio_id)
    if not db_audio:
        raise HTTPException(status_code=404, detail="Audio no encontrado")
    return db_audio

@router.post("/", response_model=schemas.Audio, status_code=201)
def crear_audio(audio: schemas.AudioCreate, db: Session = Depends(get_db)):
    return crud.create(db, audio)

@router.delete("/{audio_id}", response_model=schemas.Audio)
def eliminar_audio(audio_id: int, db: Session = Depends(get_db)):
    db_audio = crud.delete(db, audio_id)
    if not db_audio:
        raise HTTPException(status_code=404, detail="Audio no encontrado")
    return db_audio
