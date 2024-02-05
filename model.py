from typing import Optional
from pydantic import BaseModel
# importação de bibliotecas

class Pokemon (BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    