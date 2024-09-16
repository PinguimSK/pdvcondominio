from fastapi import FastAPI
from models import Morador
from typing import List

app = FastAPI()

moradores=[]

@app.get("/moradores", response_model=List[Morador])
async def lista_moradores():
    return moradores

@app.post("/moradores", response_model=Morador)
async def criar_morador(morador: Morador):
    moradores.append(morador)
    return morador

@app.put("/moradores/{morador_id}", response_model=Morador)
async def editar_morador(morador_id: int, morador: Morador):
    moradores[morador_id] = morador
    return morador

@app.delete("/moradores/{morador_id}")
async def deletar_morador(morador_id: int):
    del moradores[morador_id]
    return {"message": "Morador Deletado"}