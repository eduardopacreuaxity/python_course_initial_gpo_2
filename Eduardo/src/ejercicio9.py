# Herencia y composicion

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hace un sonido")


class Perro(Animal):
    def __init__(self, nombre = "Perro"):
        super().__init__(nombre)

    def hablar(self):
        print("Guau")

animal = Animal('Gato')
perro = Perro()

animal.hablar()
perro.hablar()
print(animal.nombre)
print(perro.nombre)