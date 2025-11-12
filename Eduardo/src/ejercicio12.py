class Notificador:
    def envia_mensaje(self, msg: str):
        print(f"Notificación enviada: {msg}")
        return msg
    
    def cancelar(self, msg: str):
        print(f"Notificación cancelada: {msg}")
        return msg
