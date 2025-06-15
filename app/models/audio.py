from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database.base import Base

class Audio(Base):
    __tablename__ = "audio"

    aud_int_id = Column(Integer, primary_key=True, index=True)
    aud_txt_nombre = Column(String(255), nullable=True)
    aud_txt_ruta_archivo = Column(Text, nullable=True)
    aud_fec_subida = Column(DateTime, default=datetime.utcnow)
    espectrogramas = relationship("Espectrograma", back_populates="audio", cascade="all, delete")
