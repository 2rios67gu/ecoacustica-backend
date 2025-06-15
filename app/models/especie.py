from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Especie(Base):
    __tablename__ = "especie"

    esp_int_id = Column(Integer, primary_key=True, index=True)
    esp_txt_nombre_cientifico = Column(String(255), nullable=False)
    esp_txt_nombre_comun = Column(String(255), nullable=False)
