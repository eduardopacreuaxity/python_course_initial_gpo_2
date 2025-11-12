from src.ejercicio12 import Notificador

def test_enviar():
    notifica = Notificador()
    msg = notifica.envia_mensaje("Mensaje")
    assert "Mensaje" in msg

def test_cancelar():
    notifica = Notificador()
    msg = notifica.cancelar("Mensaje")
    assert "Mensaje" in msg