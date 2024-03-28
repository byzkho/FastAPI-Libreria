# Importamos la clase fastapi del modulo FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# Instanciamos la clase
app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

# http://127.0.0.1:8000
@app.get('/')  # Creamos la ruta raiz
def index():  # Desarrollamos la funcion que se va a ejecutar cuando pngamos esa ruta
    return {"message": "Hello World"}

@app.get('/libros/{id}')
def mostrar_libro(id: int):
    return {'data': id}

@app.post('/libros')
def insertar_libro(libro: Libro):
    return {'message': f"Libro {libro.titulo} insertado"}
