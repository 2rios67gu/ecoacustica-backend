from pydantic import BaseModel
from datetime import datetime

class EspectrogramaBase(BaseModel):
    aud_int_id: int
    esp_txt_ruta_imagen: str

class EspectrogramaCreate(EspectrogramaBase):
    pass

class EspectrogramaOut(EspectrogramaBase):
    esp_int_id: int
    esp_fec_generado: datetime

    class Config:
        from_attributes = True
