from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.base import SessionLocal

router = APIRouter(prefix="/health", tags=["health"])

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", summary="Verifica conexión a la base de datos")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "ok", "message": "Conexión exitosa con la base de datos ✅"}
    except Exception as e:
        return {"status": "error", "message": "Error al conectar a la base de datos ❌", "detail": str(e)}
