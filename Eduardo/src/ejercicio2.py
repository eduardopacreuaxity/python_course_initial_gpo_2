# Mapas
def elevar_al_cuadrado(num_1: int) -> int:
    return num_1 ** 2

lista = [1, 2, 3]
# operation = map(lambda num_1 : num_1 ** 2, range(5))
operation = map(elevar_al_cuadrado, range(5))
result = list(operation)

print('Lista al cuadrado: ', result)