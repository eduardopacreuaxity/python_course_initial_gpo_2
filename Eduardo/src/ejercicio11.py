# Dataclasses

from dataclasses import dataclass

@dataclass
class Procesador:
    marca: str
    nucleos: int

@dataclass
class Memoria:
    tamano: int
    velocidad: float

@dataclass
class Computadora:
    procesador: Procesador
    memoria: Memoria

    def __str__(self):
        return (f"**********************************\n"
        "Procesador\n"
        f"Marca: {self.procesador.marca}\n"
        f"Nucleos: {self.procesador.nucleos}\n"
        f"Memoria\n"
        f"Tamaño: {self.memoria.tamano}\n"
        f"Velocidad: {self.memoria.velocidad}\n"
        f"**********************************")

computadora = Computadora(Procesador("Intel", 8), Memoria(8, 2.4))
print(computadora)