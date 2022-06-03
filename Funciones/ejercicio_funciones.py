# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:16:01 2022

@author: Jun
"""

"""Ejercicio 1
Escribir una función que muestre por pantalla el
saludo ¡Hola amiga! cada vez que se la invoque."""
def ej1():
    print("Hola amiga")
ej1()

"""Ejercicio 2
Escribir una función a la que se le pase una
cadena <nombre> y muestre por pantalla el saludo ¡hola
<nombre>!."""
def ej2(nombre):
    print("Hola "+nombre)
nombre = input("Dime tu nombre: ")
ej2(nombre)

"""Ejercicio 3
Escribir una función que reciba un número entero positivo y
devuelva su factorial."""
def ej3(num):
    for i in range(1,num):
        num *= i
    print("El factorial es: ",num)
num = int(input("Dame un numero: "))
ej3(num)
"""Ejercicio 4
Escribir una función que calcule el total de una factura tras
aplicarle el IVA. La función debe recibir la cantidad sin IVA
y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de
IVA, deberá aplicar un 21%."""
def ej4(num,iva):
    if iva == 0:
        total = num + num*21/100
    else:
        total = num + num*iva/100
    print("Total de factura: ",total)
num = float(input("Total factura sin iva: "))
iva = float(input("IVA: "))
ej4(num, iva)
"""Ejercicio 5
Escribir una función que calcule el área de un círculo y otra
que calcule el volumen de un cilindro usando la primera
función."""
import math
def ej5 (radio):
    area = math.pi*radio^2
    print("El area del circulo es: ",area)
    return area
radio = float(input("Radio del circulo: "))
ej5(radio)
def cilindro(ej5,altura):
    print("El volumen del cilindo es: ",ej5*altura)
altura = float(input("Altua del cilindo: "))
cilindro(ej5, altura)
"""Ejercicio 6
Escribir una función que reciba una muestra de números en
una lista y devuelva su media."""
def ej6(lista):
    media = 0
    for i in range(len(lista)):
        media = media + lista[i]
    media  = media / len(lista)
    print("La media es: ",media)
lista = input("Dame una lista de numeros separados por comas: ")
lista = lista.split(",")
lista = map(int, lista)
ej6(lista)
"""Ejercicio 7

Escribir una función que reciba una muestra de números en
una lista y devuelva otra lista con sus cuadrados."""
def ej7(lista):
    lista2 = []
    for i in lista:
        num = i**2
        lista2.append(num)
    return lista2
lista = input("Dame una lista de numeros separados por comas: ")
lista = lista.split(",")
lista = list(map(int, lista))
lista = ej7(lista)
print(lista)
"""Ejercicio 8
Escribir una función que reciba una muestra de números en
una lista y devuelva un diccionario con su media, varianza y
desviación típica."""
def ej8(lista):
    dic = {}
    media = 0
    media2 = 0
    varianza = 0
    for i in lista:
        media += i
        media2 += i**2
    media3 = media/len(lista)
    desviacion = (media2/len(lista)-media3**2)**(1/2)
    for i in lista:
        varianza += (i-media3)*2
    varianza = varianza/len(lista)
    dic["Media"]= media3
    dic["Varianza"]= varianza
    dic["Desviacion"]=desviacion
    return dic
lista = input("Dame una lista de numeros separados por comas: ")
lista = lista.split(",")
lista = list(map(int, lista))
lista = ej8(lista)
print(lista)
"""Ejercicio 9
Escribir una función que calcule el máximo común divisor
de dos números y otra que calcule el mínimo común
múltiplo."""
from math import gcd
def ej9(num1,num2):
    print("El maximo comun divisor es: ",gcd(num1,num2))
    return gcd(num1,num2)
def ej92(num1,num2,ej9):
    mcm = (num1*num2)/ej9
    print("El minimo comun multiplo es: ",mcm)
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
ej9(num1,num2)
ej92(num1, num2, ej9)
"""Ejercicio 10
Escribir una función que convierta un número decimal en
binario y otra que convierta un número binario en decimal."""

def binario(num):
    print("El numero binario de ",num," es ",bin(num))
    return bin(num)
def decimal(num):
    print("El numero decimal es: ",int(num))
    
binario(10)
bina = bin(binario(10))
decimal(bina)


"""Ejercicio 11
Escribir un programa que reciba una cadena de caracteres
y devuelva un diccionario con cada palabra que contiene y
su frecuencia. Escribir otra función que reciba el diccionario
generado con la función anterior y devuelva una tupla con
la palabra más repetida y su frecuencia."""

def ej11(frase):
    dic = {}
    palabra = frase.split(" ")
    for i in palabra:
        contador = 0
        for j in palabra:
            if i in j:
                contador += 1
        dic[i] = contador
    return dic

def ej112(dic):
    maximo = max(dic, key=dic.get)
    print("La palabra ",maximo, " aparece ",max(dic.values())," veces")
frase = input("Dame una palabra: ")
dic = ej11(frase)
ej112(dic)