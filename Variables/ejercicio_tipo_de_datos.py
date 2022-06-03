import mysql.connector
print("Ejercicio1-----------")
print("¡Hola mundo!")
print("Ejercicio2-----------")
hola_mundo = "¡Hola mundo!"
print(hola_mundo)
print("Ejercicio3-----------")
nombre = input("Como te llamas? ")
print("¡Hola " + nombre + "!")
print("Ejercicio4-----------")

print("Ejercicio5-----------")
horas_trabajadas = int(input("Cuantas horas trabajas? "))
coste_por_hora = int(input("Cuanto cobras por hora? "))
sueldo =horas_trabajadas * coste_por_hora
print("tu sueldo es: " , sueldo)
print("Ejercicio6-----------")
numero = int(input("Dame un numero: "))
suma = numero * (numero + 1) / 2
print("La suma es ",suma)
print("Ejercicio7-----------")
peso = int(input("Cuanto pesas? "))
altura = int(input("Cuanto mides en cm? "))
imc = peso/(altura/100)
print("Tu indice de masa corporal es ", round(imc,2))
print("Ejercicio8-----------")
num1 = int(input("dame un numero: "))
num2 = int(input("dame otro numero: "))
cociente = num1//num2
resto = num1%num2
print(num1, " entre ",num2, " da un cociente de :", cociente ," y un resto de ", resto)
print("Ejercicio9-----------")
inversion = int(input("Cuanto quieres invertir? "))
interes_anual = int(input("Cuanto de interes anual? "))
anos = int(input("Durante cuantos años? "))
total = (inversion*anos)-((inversion*anos)*interes_anual/100)
print("Total obtenido: ", total)
print("Ejercicio10-----------")
payasos = int(input("Cuantos payasos se han vendido? "))
munecas = int(input("Cuantas muñecas se han vendido? "))
peso_payasos = 112*payasos/1000
peso_munecas = 75*munecas/1000
peso_total = peso_payasos + peso_munecas
print("El peso total del paquete sera de ",peso_total," kg")
print("Ejercicio11-----------")
cuenta = int(input("Cuanto tienes en la cuenta de ahorros? "))
cuenta += cuenta*4/100
print("Primer año: ",cuenta)
cuenta += cuenta*4/100
print("segundo año ", cuenta)
cuenta += cuenta*4/100
print("Tercer año: ", cuenta)
print("Ejercicio12-----------")
vendido = int(input("Barras vendidas que no son del dia: "))
coste=3.49
descuento = coste - (coste *60/100)
print("El precio por barra es de ",coste," el descuento por no estar fresco es de 60%")
sin_descuento = coste*vendido
print("El coste total sin descuento es ",round(sin_descuento,2))
con_descuento = descuento*vendido
print("El coste con descuento es de " , round(con_descuento,2))