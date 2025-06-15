from pydantic import BaseModel

class EspecieBase(BaseModel):
    esp_txt_nombre_cientifico: str
    esp_txt_nombre_comun: str

class EspecieCreate(EspecieBase):
    pass

class EspecieUpdate(EspecieBase):
    pass

class EspecieInDB(EspecieBase):
    esp_int_id: int

    class Config:
        from_attributes = True
