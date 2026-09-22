import random

def tirar_dados():
    return random.randint(1,21)



print("")
print("=======================================")

def pedir_respuesta():
    print("Ingresa tu predicción")
    print("1. Par")
    print("2. Impar")
    print("3. Salir del juego")

    return int(input())


def imprimir_resultado(numero, prediccion):
#not, %
#Saber si un número es par o impar
#Dividirlo entre 2 y si es remanente es 0, es par, Si es 1, es impart

    es_par = numero % 2 == 0
    if es_par and prediccion == 1:
        print("Ganaste!, número de los dados:", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste!, número de los dados:", numero)
    else:
        print("Perdiste!, número de los dados:", numero)


while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)

print("Gracias por jugar")