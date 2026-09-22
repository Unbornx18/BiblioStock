#Funciones
def saludar(nombre, lenguaje):
    print("Hola ", nombre, "bienvenido al lenguaje de programación: ", lenguaje)

    #invocar la función con argumentos
    saludar("Trainer", "Python")
    saludar("camper", "Pseint")
    saludar()

    def compras(productos):
        print(productos)

    compras("Camisa","Televisor","Computador", "Celular")

    #Función de promedio de notas de una persona
    def calcular_promedio_3notas(nota1=0,nota2=0,nota3=0):
        promedio=(nota1+nota2+nota3)/3
        mensaje=f"El promedio de las 3 notas es: {promedio:2f}"
        return mensaje
    print(calcular_promedio_3notas(70, 80, 90))
    print(calcular_promedio_3notas())
    print(calcular_promedio_3notas(90))

#sub-funciones: Funciones dentro de funciones
def funcion_externa(x):
    def funcion_interna(y):
        return x+y
    return funcion_interna

subfunción1=funcion_externa(10)
print(subfunción1(5)) #Devuelve 15  


#Cajero automático. Calcular cuántos billetes de cada denominación debe entregar un cajero automático
#Dado un monto que el usuario pida retirar
def retiro_denominacion_billetes():
    cantidad=int(input("Ingrese la cantidad a retirar: "))
    cincuenta_mil=0
    veinte_mil=0
    diez_mil=0
    cinco_mil=0 

    while cantidad>=50000:
        cantidad-=50000
        cincuenta_mil+=1    
    while cantidad>=20000:
        cantidad-=20000
        veinte_mil+=1
    while cantidad>=10000:
        cantidad-=10000
        diez_mil+=1 
    while cantidad>=5000:
        cantidad-=5000
        cinco_mil+=1
   

    print(f"Billetes de 50,000: {cincuenta_mil}")
    print(f"Billetes de 20,000: {veinte_mil}")
    print(f"Billetes de 10,000: {diez_mil}")
    print(f"Billetes de 5,000: {cinco_mil}")

retiro_denominacion_billetes()



#Alcance de las variables
persona="Elon Musk"

def campuslands():
    persona="Johlver"

    campuslands()
    print("La persona es:",persona)