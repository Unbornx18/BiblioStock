print ("Hello, World!")

Boolean_verdadero = True
Boolean_falso = False


Numa = 5
Numb = 10

#f Es formato o que la cadena de caracteres le podemos introductir variables

print(f"Los numeros impresos son {Numa} y {Numb}")

#Operaciones básicas sobre cadenas de texto o strings

cadena = "Esto es una cadena"
primer_caracter = cadena[0]
#Voy a imprimir el primer caracter de la variable cadena

print(cadena[0:18])

indice=cadena.find("cadena")
print(indice)

#replace() reemplaza una palabra por otra, Sin modificar la cadena original
nueva_cadena = cadena.replace("cadena", "variable")
print(nueva_cadena)

otra_cadena = "Hello, World!"

#upper() lo pone en mayúsculas
#lower() lo pone en minúsculas
#capitalize() pone la primera letra en mayúscula y el resto en minúscula
#title() pone la primera letra de cada palabra en mayúscula
print(otra_cadena.upper())
print(otra_cadena.lower())
print(otra_cadena.capitalize())
print(otra_cadena.title())

la_cadena = "Hola, Mundo, Python, Programación"

#split() separa las cadenas y crea una lista, usar las comas, como referencia de corte
subcadena=la_cadena.split(",")
print(subcadena)

#join(), une los elementos de una lista en una sola cadena usando un elemento separador
cadena_unida = " - ".join(subcadena)
print(cadena_unida)

#Operadores 

numero1 = 0
numero2 = 5

#numero1 = numero1 + 1 
numero1+= 1 
print(numero1)

numero1=5
numero2/=5
print(numero2)

#Operadores relacionales
variable1=5
variable2=10

print(variable1==variable2) #Si es igual a
print(variable1!=variable2) #Si es diferente a
print(variable1>variable2) #Si es menor que
print(variable1<variable2) #Si es mayor que

#Operadores lógicos
# and, or, not
# and = las 2 respuestas o las 2 opciones deben ser verdaderas para que la respuesta sea verdadera

hay_luz=True
hay_internet=True

print("Se puede hacer la clase")
print(hay_luz and hay_internet)

#or Al menos una de las 2 opciones debe ser verdadera para que la respuesta sea verdadera

compania_padre=True
compania_madre=False

print("Puede ir el niño al parque")
print(compania_madre or compania_padre)

#not invierte el resultado lógico

que_tienes=False
print(not(que_tienes))

#Condicionales en Python
#Si la condición se cumple, se ejecuta el bloque de código dentro del if, si no se cumple, se ejecuta el bloque de código dentro del else

edad=28
if edad<=14:
    print("Eres un niño")
elif edad<=18:
    print("Eres un joven")
elif edad<=65:
    print("Eres un adulto")
else:
    print("Eres un anciano")


#Un programa para que me busque un carácter y me devuelva el índice
palabra = "programación"
#len() devuelve la longitud de la cadena para medir la longitúd de x palabra
letra_buscada= "c"
indice = 0 

while (True):
    if (indice >= len(palabra)): # Control para no salirnos del rango de la palabra
        print("No se encontró la letra")
        break # Si llega a esta parte, se sale del bucle
    if (palabra[indice] == letra_buscada):
        print("La letra está en la posición: ", indice)
        break # Si llega a esta parte, se sale del bucle
    indice+=1 # Incrementamos el índice para seguir buscando

#Estructura repetitiva for
for numero in range(30, 42, 2): # Va a iterar desde el 1 hasta el 10
    print(numero)   

#Contar cuántas veces aparece la letra  en una cadena
cadena=input ("Ingrese una cadena de texto para saber si tiene letras a:  ")
cuenta=0
for caracter in cadena:
    if caracter == "a":
        cuenta+=1   
        
print("La letra 'a' aparece", cuenta, "veces en la cadena.")
