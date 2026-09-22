print("Escribe tu nombre")
nombre = input()
print("Escribe tu edad")
edad = int(input())

#elif
#Operadores lógicos
#and (y) / or (o)
#and: todas las expresiones sean True
#or: Con que una de las expresioens sea True

''' if nombre == "Camilo":
    print("Saludos Camilo")
elif nombre == "Santiago":
    print("Qué bonito nombre, Santiago")
elif nombre == "Juan":
    print("Qué bonito nombre, Juan")
else: 
    print("Qué extraño nombre") '''

""" if nombre == "Camilo" and edad > 20:
    print("Saludos Camilo, eres un adulto")
elif nombre == "Camilo" and edad <= 20:
    print("Saludos Camilo, eres un Joven")
else:
    print("Saludos")"""

if nombre == "Camilo" or nombre == "Santiago":
    print("Me gusta tu nombre")
else:
    print("Qué nombre tan extraño")