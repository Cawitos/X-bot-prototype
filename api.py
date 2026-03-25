from fastapi import FastAPI
from pydantic import BaseModel
from main import analizar_post

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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