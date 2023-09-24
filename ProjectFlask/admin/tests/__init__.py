from src.web import create_app

app = create_app(env="test")  # <-- crea la aplicación en modo test
client = app.test_client()  # <-- crea un cliente para testear la aplicación
