from fastapi import FastAPI, UploadFile

from model import load_model, format_image
from schemas import PredictResponse

app = FastAPI(openapi_tags=[{'name': 'First Endpoint', 'description': 'First API Endpoint'}])
cats_vs_dogs_model = load_model()


# Vistas: Una función que recibe una petición (request) y da una respuesta
@app.get('/hola-mundo/{n_user}', tags=["First Endpoint"])
def get_saludo(n_user: int, mostrar_extras: bool = False):  # Type hinting
    """Saludar a los usuarios de nuestra API."""
    mensaje = f"Hola usuario número {n_user}"
    if mostrar_extras:
        return mensaje + ". Este es un dato extra"
    return mensaje


@app.get('/demo', tags=["Cats vs. Dogs Demo"], response_model=PredictResponse)
def get_demo_response():
    """Devuelve una respuesta del modelo cats_vs_dogs a una imagen almacenada en el servidor."""
    x = format_image('test_img/dog.jpg')
    response = cats_vs_dogs_model.predict(x)[0][0]
    return {"prob": response, "label": 'perro' if response > 0.5 else 'gato'}


@app.post('/predict', tags=["Cats vs. Dogs Inference"], response_model=PredictResponse)
async def post_image_to_predict(file: UploadFile):
    content = await file.read()
    x = format_image(content=content)
    response = cats_vs_dogs_model.predict(x)[0][0]
    return {"prob": response, "label": 'perro' if response > 0.5 else 'gato'}
