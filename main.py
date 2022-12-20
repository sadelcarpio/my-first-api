from fastapi import FastAPI
app = FastAPI(openapi_tags=[{'name': 'First Endpoint', 'description': 'First API Endpoint'}])


# Vistas: Una función que recibe una petición (request) y da una respuesta
@app.get('/hola-mundo/{n_user}', tags=["First Endpoint"])
def get_saludo(n_user: int, mostrar_extras: bool = False):  # Type hinting
    """Saludar a los usuarios de nuestra API."""
    mensaje = f"Hola usuario número {n_user}"
    if mostrar_extras:
        return mensaje + ". Este es un dato extra"
    return mensaje
