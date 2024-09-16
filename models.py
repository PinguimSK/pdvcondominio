from pydantic import BaseModel

class Morador(BaseModel):
    id: int
    nome: str
    cpf: str