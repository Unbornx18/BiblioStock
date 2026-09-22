from datetime import datetime

print("*****************************")
print("******* BIENVENIDO A  ******")
print("**  LA TIENDA DE MASCOTAS  **")
print("*****************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25
num_total_animales = num_perros+num_gatos+num_pajaros

print("Por favor ingresa tu nombre:")
nombre = input()
print("Por favor ingresa tu apellido:")
apellido = input()

nombres_completo = nombre + " " + apellido
print("Gracias por visitarnos", nombres_completo)

compras = []

def mostrar_menu():
    print("")
    print("===============================================")
    print("Selecciona la opción que deseas:")
    print("1: conocer cuántos animales tiene la tienda")
    print("2: comprar un animal")
    print("3: Mostrar compras")
    print("4: Salir del programa")
def mostrar_inventario():
    print("En la tienda hay", num_total_animales,"animales en total")

def comprar_animal():
    carrito = []

    while True:
        print("¿Qué animal deseas comprar? (Solo puedes elegir 1 de cada especie)")
        print("Escribe F para terminar la lista, o v para ver tu carrito")
        animal = input()

        if animal == "F":
            break
        if animal == "V":
            print(f"Tu carrito de compras contiene{carrito}")
            continue

        if animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en el carrito")

        carrito.append(animal)

    print("El contenido de tu carrito es")
    for animal in carrito:
        print("   ", animal)


    #print("Haz comprado un:", animal)
    #print("Actualmente contamos con:")
    #print("Perros:", num_perros)
    #print("Gatos:", num_pajaros)
    #print("Pajaros", num_pajaros)
    fecha = datetime.now()
    compras.append( (nombre, carrito, fecha) )

def mostrar_compras():
    print("")
    print("******** COMPRAS REALIZADAS *******")
    for compra in compras:
        print(f"      {compra[0]} compró {compra[1]} en {compra[2]}")


while True:
    mostrar_menu()
    respuesta = int(input())
    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Saliendo del programa")
        break


