import ollama
import json


def analizar_texto(texto: str):
    try:
        respuesta = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Analiza este texto y responde solamente con un JSON.

El JSON tiene que tener estos campos:
sentiment
summary
topics

Sentiment puede ser: positive, negative o neutral.

Texto:
{texto}
"""
                }
            ]
        )

        resultado = respuesta["message"]["content"]

        resultado = resultado.replace("```json", "")
        resultado = resultado.replace("```", "")
        resultado = resultado.strip()

        return json.loads(resultado)

    except Exception as error:
        return {
            "error": "No se pudo analizar el texto",
            "detalle": str(error)
        }