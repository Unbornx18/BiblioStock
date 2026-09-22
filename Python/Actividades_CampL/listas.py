#Listas
#Lista vacia
mi_lista=[]

#Lista con elementos
lista_elementos=["Tierra","Aire","Agua","Fuego"]

#Listas con diferentes datos
lista_heterogenias=["Caracteres", 20 , 78.4 , True]

#Listas anidadas, matrices
matriz1=[["codigo","nombre","fecha"],[123,"Juan velandia", "2000-12-12"],[456,"Juan Ardila", "2006-01-01"]]

print(matriz1[2][1],matriz1[1][1])

#Metodos de listas, append me agrega un elemento al final
lista_elementos.append("Plasma")
print(lista_elementos)

#Extend, agregar una lista a otra
lista_heterogenias.extend(lista_elementos)
print(lista_heterogenias)

#Insertar un elemento en una posicion especifica
lista_heterogenias.insert(0,"Rayo Mqueen")
print(lista_heterogenias)

materias=["Sandbox", "Introducción a la programación", "Python"]

#ndex me devuelve la pos del elemento
notas=[0,6.75,5.67,0]
notas.remove(0)
print(notas)

#Eliminar todos los elementos de la lista
notas.clear()
print(notas)