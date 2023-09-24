from tests import client


def test_web():
    """Testea que la aplicación web funcione correctamente"""
    response = client.get("/")
    assert b"Inicio" in response.data
