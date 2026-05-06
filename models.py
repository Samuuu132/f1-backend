from pydantic import BaseModel
from typing import Optional

class DriverCreate(BaseModel):
    nombre: str
    equipo: str
    nacionalidad: str
    numero: int
    imagen: Optional[str] = None