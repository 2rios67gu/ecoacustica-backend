from sqlalchemy.orm import Session
from app.models.resultado_identificacion import ResultadoIdentificacion
from app.schemas.resultado_identificacion import ResultadoIdentificacionCreate

def get_all_resultados(db: Session):
    return db.query(ResultadoIdentificacion).all()

def get_resultado_by_id(db: Session, resultado_id: int):
    return db.query(ResultadoIdentificacion).filter(ResultadoIdentificacion.res_int_id == resultado_id).first()

def create_resultado(db: Session, resultado: ResultadoIdentificacionCreate):
    db_resultado = ResultadoIdentificacion(**resultado.dict())
    db.add(db_resultado)
    db.commit()
    db.refresh(db_resultado)
    return db_resultado

def delete_resultado(db: Session, resultado_id: int):
    db_resultado = get_resultado_by_id(db, resultado_id)
    if db_resultado:
        db.delete(db_resultado)
        db.commit()
    return db_resultado
