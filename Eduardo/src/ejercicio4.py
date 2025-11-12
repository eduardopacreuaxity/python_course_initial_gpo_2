# args y kwargs

def saludos(*args) -> None:
    print(f"Argumentos por posicion: {args}")

saludos("lalo", "pepe")

def saludos_dinamicos(**kwargs) -> None:
    print(f"Argumentos por nombre: {kwargs}")

saludos_dinamicos(nombre="lalo", edad="30")

# Generadores

def generar_datos(limite: int):
    print("INICIO")
    for num in range(limite):
        print(f"Bucle en posicion {num}")
        yield num
    print("FIN")

def generar_datos_tradicional(limite: int):
    print("INICIO TRADICIONAL")
    resultado = []
    for num in range(limite):
        print(f"Bucle en posicion {num}")
        resultado.append(num)
    print("FIN TRADICIONAL")
    return resultado

print("USAR GENERADOR")
generador = generar_datos(5)
print(type(generador))

for item in generador:
    print(f"Valor generado: {item}")