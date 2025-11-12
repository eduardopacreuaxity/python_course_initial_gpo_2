# Decoradores

def saludar():
    print("Hola Mundo")

def decorador(func):
    def envoltura():
        print("INICIO")
        func()
        print("FIN")
    return envoltura
 
saludo_decorado = decorador(saludar)
saludo_decorado()

@decorador
def saludar1():
    print("Hola Mundo")

saludar1()


# Decorador con argumentos
def decorador1(func):
    def envoltura(*args, **kwargs):
        print(f"INICIO CON ARGS {args} o KWARGS {kwargs}")
        func(*args, **kwargs)
        print("FIN")
    return envoltura

@decorador1
def suma(n1: int, n2: int) -> None:
    print(f"La suma es: {n1 + n2}")

suma(3, 5)