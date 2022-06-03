# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:18:46 2022

@author: Jun
"""

"""Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es
mayor de edad o no."""
edad = int(input("Dame una edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas."""
psw = input("Introduce una contraseña: ")
psw2 = input("Repita la contraseña: ")
if psw.lower() == psw2.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error."""
num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
if num2 == 0:
    print("Error, el divisor no puede ser 0")
else:
    division = num1/num2
    print("El resultado de la division es: ",division)
"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es par o impar."""
num = int(input("Dame un numero: "))
if num % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")
"""Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
que tributar o no."""
edad = int(input("Dame una edad: "))
if edad >= 16:
    ingresos = int(input("Cuanto ingresas al año: "))
    if ingresos>1000:
        print("Tienes que tributar")
    else:
        print("No superas los 1000")
else:
    print("No tienes edad para tributar")
"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
corresponde."""
nombre = input("Dame un nombre: ")
sexo = input("Dame un sexo H o M: ")
if sexo == H:
    if nombre.lower() > "n":
        print("Grupo A")
    else:
        print("Grupo B")
else:
    if nombre.lower() < "m":
        print("Grupo A")
    else:
        print("Grupo B")
"""Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:

Renta Tipo impositivo

Menos de 10000€ 5%

Entre 10000€ y 20000€ 15%

Entre 20000€ y 35000€ 20%

Entre 35000€ y 60000€ 30%

Más de 60000€ 45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
tipo impositivo que le corresponde."""
renta = int(input("Dime tu renta anual: "))
if renta < 10000:
    print("Tienes que pagar un 5% de impuestos")
elif renta >= 10000 and renta < 20000:
    print("Tienes que pagar un 15% de impuestos")
elif renta >= 20000 and renta < 35000:
    print("Tienes que pagar un 20% de impuestos")
elif renta >= 35000 and renta < 60000:
    print("Tienes que pagar un 30% de imppuestos")
elif renta >= 60000:
    print("Tienes que pagar un 45% de impuestos")
"""Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las
cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
es de 2.400€ multiplicada por la puntuación del nivel.
Nivel Puntuación

Inaceptable 0.0

Aceptable 0.4

Meritorio 0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario."""
sueldo = 2400
puntuacion = float(input("Dime tu valoracion (0,0.4,0.6): "))
if puntuacion == 0:
    sueldo = sueldo + sueldo*puntuacion
    print("Tu sueldo sera ",sueldo)
elif puntuacion == 0.4:
    sueldo = sueldo + sueldo*puntuacion
    print("Tu sueldo sera ",sueldo)
elif puntuacion == 0.6:
    sueldo = sueldo + sueldo*puntuacion
    print("Tu sueldo sera ",sueldo)
"""Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre
4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""
edad = int(input("Dime tu edad: "))
if edad < 4:
    print("Entras gratis")
elif edad >= 4 and edad < 18:
    print("Tienes que pagar 5 euros")
elif edad >= 18:
    print("Tienes que pagar 10 europs")
"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
 Ingredientes vegetarianos: Pimiento y tofu.
 Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que
están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva."""
piza_vegetariana = ["pimiento","tofu"]
piza_no_vegetariana = ["peperoni","jamon","salmon"]
piza = input("Quieres una piza vegetariana? [si/no]")
if(piza == "si"):
    mozarela = input("Quieres añadir queso mozarela? [si/no]: ")
    piza_vegetariana.append("mozarela")
    print("Tu piza vegetariana tiene: ",piza_vegetariana)
else:
    mozarela = input("Quieres añadir queso mozarela? [si/no]: ")
    piza_no_vegetariana.append("mozarela")
    print("Tu piza no vegetariana tiene: ",piza_no_vegetariana)