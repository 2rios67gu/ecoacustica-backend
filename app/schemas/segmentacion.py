from pydantic import BaseModel
from datetime import datetime

class SegmentacionBase(BaseModel):
    esp_int_id: int
    seg_txt_ruta_imagen: str

class SegmentacionCreate(SegmentacionBase):
    pass

class SegmentacionOut(SegmentacionBase):
    seg_int_id: int
    seg_fec_procesado: datetime

    class Config:
        from_attributes = True
