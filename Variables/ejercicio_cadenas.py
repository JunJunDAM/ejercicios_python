# -*- coding: utf-8 -*-
"""
Created on Mon May 23 18:31:42 2022

@author: Jun
"""

"""Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la
consola y un número entero e imprima por pantalla en líneas
distintas el nombre del usuario tantas veces como el número
introducido."""
nombre = input("Dime tu nombre: ")
cant = int(input("Dime un numero: "))
for i in range (cant):
    print(nombre)
"""Ejercicio 2
Escribir un programa que pregunte el nombre completo del
usuario en la consola y después muestre por pantalla el
nombre completo del usuario tres veces, una con todas las
letras minúsculas, otra con todas las letras mayúsculas y otra
solo con la primera letra del nombre y de los apellidos en
mayúscula. El usuario puede introducir su nombre combinando
mayúsculas y minúsculas como quiera."""
nombre = input("Dame tu nombre: ")
print(nombre.lower())
print(nombre.title())
print(nombre.upper())
"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la
consola y después de que el usuario lo introduzca muestre por
pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el
nombre de usuario en mayúsculas y <n> es el número de letras
que tienen el nombre."""
nombre = input("Dame un nombre: ")
print(nombre.upper()," tiene ",len(nombre)," letras")
"""Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato
prefijo-número-extension donde el prefijo es el código del
país +34, y la extensión tiene dos dígitos (por ejemplo
+34-913724710-56). Escribir un programa que pregunte por un
número de teléfono con este formato y muestre por pantalla el
número de teléfono sin el prefijo y la extensión."""
print("Dame un telefono con el siguiente formato: +34-913724710-56 ")
numero = input("tu numero: ")
num = numero.split("-")
print(num[1])
"""Ejercicio 5
Escribir un programa que pida al usuario que introduzca una
frase en la consola y muestre por pantalla la frase invertida."""
frase = input("Dame una frase: ")
invertir = "".join(reversed(frase))
print("frase invertida: ", invertir)
"""Ejercicio 6
Escribir un programa que pida al usuario que introduzca una
frase en la consola y una vocal, y después muestre por
pantalla la misma frase pero con la vocal introducida en
mayúscula."""
frase = input("dame una frase")
vocal = input("dame una vocal")
print(frase,vocal.upper)
"""Ejercicio 7
Escribir un programa que pregunte el correo electrónico del
usuario en la consola y muestre por pantalla otro correo
electrónico con el mismo nombre (la parte delante de la arroba
@) pero con dominio ceu.es."""
correo = input("Dame un correo")
correo1 = correo.split("@")
print(correo1[0]+"@ceu.es")
"""Ejercicio 8
Escribir un programa que pregunte por consola el precio de un
producto en euros con dos decimales y muestre por pantalla el
número de euros y el número de céntimos del precio
introducido."""
precio = input("Dame un precio: ")
precio1 = precio.split(",",".")
print(precio1[0]+" Euros con " + precio[1] + " centimos")
"""Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el
día, el mes y el año. Adaptar el programa anterior para que
también funcione cuando el día o el mes se introduzcan con un
solo carácter."""
print("dame una fecha con formato dd/mm/aaaa")
cumple = input("Fecha: ")
cumple1 = cumple.split("/")
print("Dia: "+ cumple1[0]+" Mes: "+ cumple1[1]+" Año: " + cumple1[2])
"""Ejercicio 10
Escribir un programa que pregunte por consola por los
productos de una cesta de la compra, separados por comas, y
muestre por pantalla cada uno de los productos en una línea
distinta."""
compra = input("Lista de compra: ")
print(compra.replace(",", "\n"))

"""Ejercicio 11
Escribir un programa que pregunte el nombre el un producto,
su precio y un número de unidades y muestre por pantalla una
cadena con el nombre del producto seguido de su precio
unitario con 6 dígitos enteros y 2 decimales, el número de
unidades con tres dígitos y el coste total con 8 dígitos enteros y
2 decimales."""
producto = input("Nombre del producto: ")
precio = float(input("Precio: "))
unidades = int(input("Cantidad: "))
total = precio*unidades
print(producto,", precio: ",round(precio,2)," unidades: ",unidades," total: ", round(total,2))