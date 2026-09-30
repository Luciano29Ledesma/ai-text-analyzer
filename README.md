AI Text Analyzer API

API hecha con Python y FastAPI que permite analizar textos usando un modelo de inteligencia artificial de forma local.

Tecnologías
Python
FastAPI
Pydantic
Ollama
Llama 3.2
Qué hace

La API recibe un texto y devuelve:

Sentimiento
Resumen
Temas principales

Los resultados se devuelven en formato JSON.

Instalación

Clonar el repositorio:

git clone https://github.com/Luciano29Ledesma/ai-text-analyzer.git
cd ai-text-analyzer

Crear el entorno virtual:

python -m venv venv

Instalar las dependencias:

pip install -r requirements.txt

También es necesario tener Ollama instalado y descargar el modelo:

ollama pull llama3.2:3b
Ejecutar
uvicorn main:app --reload

Una vez iniciada la API, se puede probar desde la documentación que genera FastAPI.

Ejemplo

Entrada:

{
  "texto": "El producto llegó tarde y la atención fue mala."
}

Respuesta:

{
  "texto": "El producto llegó tarde y la atención fue mala.",
  "analisis": {
    "sentiment": "negative",
    "summary": "El cliente tuvo una experiencia negativa.",
    "topics": ["entrega", "atención"]
  }
}
Autor

Luciano Augusto Ledesma