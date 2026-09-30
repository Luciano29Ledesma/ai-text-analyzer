from fastapi import FastAPI, HTTPException
from models import TextoEntrada
from services.ai_service import analizar_texto

app = FastAPI()


@app.get("/")
def inicio():
    return {
        "mensaje": "AI Text Analyzer API"
    }


@app.post("/analizar")
def analizar(datos: TextoEntrada):
    resultado = analizar_texto(datos.texto)

    if "error" in resultado:
        raise HTTPException(
            status_code=500,
            detail=resultado
        )

    return {
        "texto": datos.texto,
        "analisis": resultado
    }