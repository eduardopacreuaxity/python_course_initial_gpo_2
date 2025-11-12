# Comentario en linea con #

'''
Comentario de bloque
Comentario multilinea
Con commillas simples o dobles
'''

# Imprimir algo en consola
print("Hola Mundo")

# Tipos de datos
variable_entera = 10
variable_flotante = 10.5
variable_cadena = "Hola"
variable_booleana = True

print(type(variable_entera))
print(type(variable_flotante))
print(type(variable_cadena))
print(type(variable_booleana))

#Estrutura de datos

# Listas
lista1 = [1, 2, 3]
print(type(lista1))

print("Lista antes de modificar: ", lista1)
lista1[2] = 4
print("Lista antes de modificar: ", lista1)

# Tuplas
tupla1: tuple = (1, 2, 3)
print(type(tupla1))


print("Tupla antes de modificar: ", tupla1)
try:
    tupla1[2] = 4
except:
    print("ERROR: Se intento cambiar una tupla")
print("Tupla antes de modificar: ", tupla1)
