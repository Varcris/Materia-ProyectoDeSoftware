from web import create_app  # <-- importa la función "create_app" del módulo "web"

app = create_app()  # <-- crea la aplicación
app.testing = True  # <-- setea el modo testing de la aplicación
client = app.test_client()  # <-- crea un cliente para testear la aplicación


def test_web():  # <-- test de la ruta "/"
    response = client.get("/")  # <-- hace un request a la ruta "/"
    assert (
        b"Hello, World!" in response.data
    )  # <-- testea que la respuesta contenga "Hello, World!"
