# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:34:41 2022

@author: Jun
"""

"""Ejercicio 1
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista y la muestre por pantalla."""

asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
print(asignaturas)

"""Ejercicio 2
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista y la muestre por pantalla el mensaje Yo
estudio <asignatura>, donde <asignatura> es cada una de
las asignaturas de la lista."""

for i in range(len(asignaturas)):
    print("Yo estudio: " + asignaturas[i])

"""Ejercicio 3
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha
sacado en cada asignatura, y después las muestre por pantalla
con el mensaje En <asignatura> has sacado <nota> donde
<asignatura> es cada una des las asignaturas de la lista y
<nota> cada una de las correspondientes notas introducidas
por el usuario."""

notas = []

for i in range(len(asignaturas)):
    nota = input("Que has sacado en "+asignaturas[i]+" ? ")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En "+ asignaturas[i]+" has sacado un "+notas[i])

"""Ejercicio 4
Escribir un programa que pregunte al usuario los números
ganadores de la lotería primitiva, los almacene en una lista y
los muestre por pantalla ordenados de menor a mayor."""

numero = []

for i in range(1,8):
    numeros = int(input("Introduce numero de primitiva: "))
    numero.append(numeros)
numero.sort()
print(numero, end=(","))

"""Ejercicio 5
Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso
separados por comas."""

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()
print(numeros)

"""Ejercicio 6
Escribir un programa que almacene las asignaturas de un
curso (por ejemplo Matemáticas, Física, Química, Historia y
Lengua) en una lista, pregunte al usuario la nota que ha
sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las
asignaturas que el usuario tiene que repetir."""

asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []
suspendidas =  []
for i in range(len(asignaturas)):
    nota = int(input("Que has sacado en "+asignaturas[i]+" ? "))
    notas.append(nota)
    if nota <= 5:
        suspendidas.append(asignaturas[i])

print("Tienes que recuperar ", suspendidas)

"""Ejercicio 7
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de
3, y muestre por pantalla la lista resultante."""

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

lista = [str(abecedario[i]) for i in range(len(abecedario)) if (i%3 != 0)]
print(lista)


"""for i in range(0,len(abecedario),3):
    abecedario.remove(i)
print(abecedario)"""

"""Ejercicio 8
Escribir un programa que pida al usuario una palabra y
muestre por pantalla si es un palíndromo."""

palabra = input("Introduce una palabra: ")
inversa = "".join(reversed(palabra))

if palabra == inversa:
    print("Es palindroma")
else:
    print("Nada")

"""Ejercicio 9
Escribir un programa que pida al usuario una palabra y
muestre por pantalla el número de veces que contiene cada
vocal."""


a = 0
e = 0
i = 0
o = 0
u = 0

palabra = input("Dame una palabra: ")

palabra = list(palabra)

for j in range(len(palabra)):
    if palabra[j] == "a":
        a += 1
    elif palabra[j] == "e":
        e +=1
    elif palabra[j] == "i":
        i +=1
    elif palabra[j] == "o":
        o +=1
    elif palabra[j] == "u":
        u +=1

print("A:",a,"E:",e,"I:",i,"O:",o,"U:",u)

"""Ejercicio 10
Escribir un programa que almacene en una lista los siguientes
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el
menor y el mayor de los precios."""

lista = [50, 75, 46, 22, 80, 65, 8]
print("Minimo: ", min(lista),"Maximo: ",max(lista))

"""Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y
(-1,0,2) en dos listas y muestre por pantalla su producto
escalar."""



"""Ejercicio 12
Escribir un programa que almacene las matrices

*mirar pizarra ; )

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas
anidadas, representando cada vector fila en una lista."""



"""Ejercicio 13

Escribir un programa que pregunte por una muestra de
números, separados por comas, los guarde en una lista y
muestre por pantalla su media y desviación típica."""
media = 0
media2 = 0
numeros = input("Lista de numeros separados por comas: ")
numeros = numeros.split(",")
numeros = list(map(int, numeros))
for i in range(len(numeros)):
    media += numeros[i]
    media2 += numeros[i]**2
media3 = media/len(numeros)
desviacion = (media2/len(numeros)-media3**2)**(1/2)
print("La media es: ",media/len(numeros))
print("La desviacion es: ",desviacion)