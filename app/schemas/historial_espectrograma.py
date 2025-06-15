from pydantic import BaseModel
from datetime import datetime

class HistorialEspectrogramaBase(BaseModel):
    esp_int_id: int
    his_txt_descripcion: str

class HistorialEspectrogramaCreate(HistorialEspectrogramaBase):
    pass

class HistorialEspectrograma(HistorialEspectrogramaBase):
    his_int_id: int
    his_fec_cambio: datetime

    class Config:
        from_attributes = True
