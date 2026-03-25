from fastapi import FastAPI
from pydantic import BaseModel
from main import analizar_post

app = FastAPI()

class PostRequest(BaseModel):
    url: str
    respuesta: str
    ganadores: int


@app.post("/analizar")
def analizar(data: PostRequest):
    resultado = analizar_post(
        data.url,
        data.respuesta,
        data.ganadores
    )
    return {"ganadores": resultado}