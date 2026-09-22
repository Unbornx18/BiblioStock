print("**************************************")
print("****   Bienvenido a WM FRUITS    *****")
print("**************************************")
print("**************************************")

print("Por favor ingresa tu nombre:")
nombre = input()
print("Por favor ingresa tu apellido")
apellido = input()

nombre_completo = nombre + " " + apellido

print("Bienvenido", nombre_completo)

manzanas = 20

print("Actualmente contamos", manzanas,"manzanas")
print("Precio: Manzana c/u $5 dólares")
print("¿Cuántas manzanas desea comprar?")


compra_manzanas = input()
cantidad_total = manzanas - int(compra_manzanas)
cantidad_total= int(cantidad_total)

print("Acabas de realizar una compra por c/u de manzanas:", compra_manzanas)
print("Actualmente queda disponible", cantidad_total, "manzanas")