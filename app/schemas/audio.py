from pydantic import BaseModel
from datetime import datetime

class AudioBase(BaseModel):
    aud_txt_nombre: str | None = None
    aud_txt_ruta_archivo: str | None = None

class AudioCreate(AudioBase):
    pass

class Audio(AudioBase):
    aud_int_id: int
    aud_fec_subida: datetime

    class Config:
        from_attributes = True
