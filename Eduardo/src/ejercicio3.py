productos = [["Manzana", 10], ["Platano", 5], ["Huevo", 3], ["Sandia", 50]]

def iva(num_1: float) -> float:
    return round(num_1 * 0.16, 2)

def ivas(product1: list) -> float:
    return round(product1[1] * 0.16, 2)

def total(num_1: float, num_2: float) -> float:
    return round(num_1 + num_2, 2)

def totals(product1: list, iva1: float) -> float:
    return round(product1[1] + iva1, 2)

productosIvas = list(map(ivas, productos))
print("IVAS:", productosIvas)

productosTotals = list(map(totals, productos, productosIvas))
print("TOTAL:", productosTotals)

print("****************************************")
print("TICKET")
print("****************************************")
'''
print("Ticket individual")
for index, product in enumerate(productos):
    productIva = iva(product[1])
    productTotal = total(product[1], productIva)
    print("PRODUCTO", index + 1)
    print("Producto: ", product[0])
    print("Precio: ", product[1])
    print("IVA: ", productIva)
    print("Total: ", productTotal)
    print("****************************************")
'''

for index1, product1 in enumerate(productos):
    print("PRODUCTO", index1 + 1)
    print("Producto: ", product1[0])
    print("Precio: ", product1[1])
    print("IVA: ", productosIvas[index1])
    print("Total: ", productosTotals[index1])
    print("****************************************")