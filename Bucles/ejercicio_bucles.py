# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:08:28 2022

@author: Jun
"""

"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces."""
palabra = input("Dame una palabra: ")
for i in range (10):
    print(palabra)
"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad)."""
edad = int(input("Dame tu edad: "))
for i in range(edad):
    i = i +1
    print("Has cumplido ", i , " años")
"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas."""
num = int(input("Dame un numero: "))
for i in range(1,num,2):
    print(i, end=(","))
"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas."""
num = int(input("Dame un numero: "))
for i in range(num):
    print(num, end=(","))
    num = num -1
"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión."""
inversion = int(input("Cuanto quieres invertir: "))
interes = float(input("interes anual [0.1-0.9]: "))
inversion = inversion + inversion*interes
anos = int(input("Cuantos años: "))
for i in range(anos):
    i = i+1
    print("Año ", i," :",inversion * i)
"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido."""
num = int(input("Dame un numero: "))
for i in range(num+1):
    print("*"*i)
"""Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""
for i in range(10):
    i = i+1
    for j in range(10):
        j = j+1
        print(i,"x",j,"=",i*j)
"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""
num = int(input("Dame un numero: "))

for i in range (1,num+1,2):
    for j in range(i,0,-2):
        print(j,end=(""))
    print("")

"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta."""
psw = "contrasena"
psw2 = input("Introduce los caracteres: contrasena: ")
while psw != psw2:
    print("Las contrasenas no coinciden")
    psw2 = input("Introduce los caracteres: contrasena: ")
    pass
print("Las contrasenas coinciden")
"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no."""
num = int(input("Dame un nunero: "))
if num % 2 != 0:
    print(num," es impar")
"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una
a una las letras de la palabra introducida empezando por la última."""
palabra = input("Dame una palabra: ")
invertir = "".join(reversed(palabra))
palabra = list(invertir)

for i in range (len(palabra)):
    print(invertir[i])

"""Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase."""
frase = input("Dame una frase: ")
letra = input("Dame una letra: ")
frase = list(frase)
contador = 0
for i in range (len(frase)):
    if frase[i] == letra:
        contador += 1
print("La letra "+ letra + " aparece",contador," veces")
"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará."""
texto = input("Escribe algo: ")
while texto != "salir":
    texto = input("Escribe algo: ")
    print(texto)
    pass
print("Se acabo")