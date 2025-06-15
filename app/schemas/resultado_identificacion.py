from pydantic import BaseModel
from datetime import datetime

class ResultadoIdentificacionBase(BaseModel):
    aud_int_id: int
    esp_int_id: int

class ResultadoIdentificacionCreate(ResultadoIdentificacionBase):
    pass

class ResultadoIdentificacion(ResultadoIdentificacionBase):
    res_int_id: int
    res_fec_identificado: datetime

    class Config:
        from_attributes = True
