from fastapi import FastAPI
from pydantic import BaseModel
from main import analizar_post
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import csv

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
    respuesta: str | None = None
    ganadores: int | None = None
    extract_usernames: bool = False
    extract_bet_ids: bool = False
    bet_type: str = "all"


@app.post("/analizar")
def analizar(data: PostRequest):
    print("Request:", data)

    try:
        resultado = analizar_post(
            url=data.url,
            respuesta=data.respuesta,
            ganadores=data.ganadores,
            extract_usernames=data.extract_usernames,
            extract_bet_ids=data.extract_bet_ids,
            bet_type=data.bet_type
        )

        print("Resultado:", resultado)

        return {
            "status": "ok",
            "data": resultado
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }

@app.post("/export")
def export(data: PostRequest):

    result = analizar_post(
        url=data.url,
        respuesta=data.respuesta,
        ganadores=data.ganadores,
        extract_usernames=data.extract_usernames,
        extract_bet_ids=data.extract_bet_ids,
        bet_type=data.bet_type
    )

    file_path = "results.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # HEADERS
        writer.writerow(["X Username", "Stake ID", "Comentario"])

        for item in result.get("ganadores", []):
            parts = item.split("|")

            x_user = parts[0].strip() if len(parts) > 0 else ""
            stake = parts[1].replace("Stake:", "").strip() if len(parts) > 1 else ""
            comment = parts[2].strip() if len(parts) > 2 else ""

            writer.writerow([x_user, stake, comment])

    return FileResponse(file_path, filename="results.csv")