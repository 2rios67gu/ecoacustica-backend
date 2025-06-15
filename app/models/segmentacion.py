from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base

class Segmentacion(Base):
    __tablename__ = "segmentacion"

    seg_int_id = Column(Integer, primary_key=True, index=True)
    esp_int_id = Column(Integer, ForeignKey("espectrograma.esp_int_id"), nullable=False)
    seg_txt_ruta_imagen = Column(Text, nullable=False)
    seg_fec_procesado = Column(DateTime, default=datetime.utcnow)

    espectrograma = relationship("Espectrograma", back_populates="segmentaciones")
