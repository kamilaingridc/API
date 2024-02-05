from typing import Optional
from pydantic import BaseModel
# importação de bibliotecas

class Pokemons (BaseModel):
    id: Optional[int] = None
    nome: str
    elemento: str
    altura: int
    