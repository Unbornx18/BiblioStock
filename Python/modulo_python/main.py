#Programa para inscripción de cursos, validar edades de los participantes, hacer cálculos de costos 
#Y si la persona va a tener descuentos

#El primero es la carpeta, el segundo el archivo
from validaciones.validaciones import validar_nombre, validar_edad
from matematicas.calculos import calcular_costo
print("======Matrícula del curso======")

nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
horas=int(input("Cuántas horas dura el curso: "))

#Validar el nombre de la persona
if not validar_nombre(nombre):
    print("Error: el nombre No puede estar vacío")
elif not validar_edad(edad):
    print("No puedes matricularte, o eres muy joven o ya eres una momia")
else:
    valor_hora=int(input("Introduce el valor por hora del curso: "))
    horas=int(input("Introduce la cantidad de horas del curso: "))
    costo=calcular_costo(horas,valor_hora)
    print(f"Bienvenido sujetó {nombre}")
    print(f"Costo del curso: {costo}")
    #Código para matricular a la persona, el nombre válido


#Intente válidar las horas del curso
#Creen una función para hacer un descuento del 10% si la persona es mayor de 65 años
