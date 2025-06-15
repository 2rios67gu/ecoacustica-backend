from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base
from datetime import datetime

class Espectrograma(Base):
    __tablename__ = "espectrograma"

    esp_int_id = Column(Integer, primary_key=True, index=True)
    aud_int_id = Column(Integer, ForeignKey("audio.aud_int_id"), nullable=False)
    esp_txt_ruta_imagen = Column(Text, nullable=False)
    esp_fec_generado = Column(DateTime, default=datetime.utcnow)

    audio = relationship("Audio", back_populates="espectrogramas")
    segmentaciones = relationship("Segmentacion", back_populates="espectrograma", cascade="all, delete")
