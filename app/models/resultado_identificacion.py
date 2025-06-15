from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.base import Base

class ResultadoIdentificacion(Base):
    __tablename__ = "resultado_identificacion"

    res_int_id = Column(Integer, primary_key=True, index=True)
    aud_int_id = Column(Integer, ForeignKey("audio.aud_int_id"), nullable=False)
    esp_int_id = Column(Integer, ForeignKey("especie.esp_int_id"), nullable=False)
    res_fec_identificado = Column(DateTime(timezone=True), server_default=func.now())
