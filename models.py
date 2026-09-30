from pydantic import BaseModel, Field


class TextoEntrada(BaseModel):
    texto: str = Field(min_length=1)