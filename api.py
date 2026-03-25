from fastapi import FastAPI
from pydantic import BaseModel
from main import analizar_post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    print("Request:", data)

    try:
        resultado = analizar_post(
            data.url,
            data.respuesta,
            data.ganadores
        )

        print("Resultado:", resultado)
        return {"ganadores": resultado}

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "error": str(e),
            "mensaje": "Error interno en el servidor"
        }