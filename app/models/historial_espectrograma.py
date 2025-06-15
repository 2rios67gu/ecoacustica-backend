from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from app.database.base import Base

class HistorialEspectrograma(Base):
    __tablename__ = "historial_espectrograma"

    his_int_id = Column(Integer, primary_key=True, index=True)
    esp_int_id = Column(Integer, ForeignKey("espectrograma.esp_int_id"), nullable=False)
    his_txt_descripcion = Column(Text, nullable=False)
    his_fec_cambio = Column(DateTime(timezone=True), server_default=func.now())
