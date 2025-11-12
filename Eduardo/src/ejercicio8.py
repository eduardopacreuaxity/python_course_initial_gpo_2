# Classes
class Producto:
    def __init__(self, nombre: str):
        ''' Constructor de la clase producto '''
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        if (len(nombre_nuevo) < 1):
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre_nuevo

producto = Producto('Lalo')
print(f"El nombre del producto es {producto.nombre}")

producto.nombre = 'Pepe'
print(f"El nombre del producto es {producto.nombre}")

producto.nombre = ''
print(f"El nombre del producto es {producto.nombre}")