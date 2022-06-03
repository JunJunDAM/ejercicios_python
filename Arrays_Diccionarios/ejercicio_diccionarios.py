# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:27:27 2022

@author: Jun
"""

"""Ejercicio 1
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al
usuario por una divisa y muestre su símbolo o un mensaje de
aviso si la divisa no está en el diccionario."""

divisa = {"Euro":"€","Dollar":"$","Yen":"¥"}
valor = input("Que divisa quieres? ")
if valor in divisa:
    print(divisa[valor])
else:
    print("Divisa no encontrada")

"""Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. Después
debe mostrar por pantalla el mensaje <nombre> tiene <edad>
años, vive en <dirección> y su número de teléfono es
<teléfono>."""

nombre = input("Dime un nombre: ")
edad = int(input("Dime una edad: "))
direccion = input("Dime una direccion: ")
telf = input("Dime un telefono: ")

agenda = {"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telf}
print(agenda["nombre"]+"tiene ",agenda["edad"]," años, vive en "+agenda["direccion"]+" y su numero de telefono es "+agenda["telefono"])

"""Ejercicio 3
Escribir un programa que guarde en un diccionario los precios
de las frutas de la tabla, pregunte al usuario por una fruta, un
número de kilos y muestre por pantalla el precio de ese
número de kilos de fruta. Si la fruta no está en el diccionario
debe mostrar un mensaje informando de ello.
Fruta Precio

Plátano 1.35
Manzana 0.80
Pera 0.85

Naranja 0.70
"""

fruteria = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
fruta = input("Dime una fruta: ")

if fruta in fruteria:
    print("La "+fruta+" esta a ",fruteria[fruta]," euros el kilo")
    kilos = float(input("Cuantos kilos quieres? "))
    total = fruteria[fruta]*kilos
    print(kilos," de "+fruta+" son ",total)
else:
    print("Fruta no disponible")

"""Ejercicio 4
Escribir un programa que pregunte una fecha en formato
dd/mm/aaaa y muestre por pantalla la misma fecha en formato
dd de <mes> de aaaa donde <mes> es el nombre del mes."""

meses = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril"
         ,"05":"Mayo","06":"Junio","07":"Julio","08":"Agosto"
         ,"09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}

fecha = input("Dime una fecha en formato [dd/mm/aaaa]: ")
dic = fecha.split("/")

if dic[1] in meses:
    print(dic[0]+" de "+meses[dic[1]]+" de "+dic[2])
else:
    print("Formato no valido")

"""Ejercicio 5
Escribir un programa que almacene el diccionario con los
créditos de las asignaturas de un curso {'Matemáticas': 6,
'Física': 4, 'Química': 5} y después muestre por pantalla
los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada
una de las asignaturas del curso, y <créditos> son sus
créditos. Al final debe mostrar también el número total de
créditos del curso."""

asignaturas =  {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
lista = list(asignaturas.keys())

for i in range(len(lista)):
    if lista[i] in asignaturas:
        print(lista[i]+" tiene ", asignaturas[lista[i]], " creditos")

print("El curso tiene ", sum(asignaturas.values()) ," creditos")

"""Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya
llenado con información sobre una persona (por ejemplo
nombre, edad, sexo, teléfono, correo electrónico, etc.) que se
le pida al usuario. Cada vez que se añada un nuevo dato debe
imprimirse el contenido del diccionario."""

persona = {}

nombre = input("Dame un nombre: ")
apellido = input("Dame un apellido: ")
edad = input("Dame una edad: ")

persona["nombre"]=nombre
persona["apellido"]=apellido
persona["edad"] = edad
print(persona)

"""Ejercicio 7
Escribir un programa que cree un diccionario simulando una
cesta de la compra. El programa debe preguntar el artículo y
su precio y añadir el par al diccionario, hasta que el usuario
decida terminar. Después se debe mostrar por pantalla la lista
de la compra y el coste total, con el siguiente formato

Lista de la
compra
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio

... ...
Total Coste"""

lista_compra = {}

while True:
    print("1-añadir productos")
    print("2-cuenta")
    o = input("Elige una opcion: ")
    if o =="1":
        producto = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        lista_compra[producto]=float(precio)
    elif o == "2":
        print("El precio de todo es: ",sum(lista_compra.values()),"€")
        break
    else:
        print("opcion no valida")

"""Ejercicio 8
Escribir un programa que cree un diccionario de traducción
español-inglés. El usuario introducirá las palabras en español e
inglés separadas por dos puntos, y cada par
<palabra>:<traducción> separados por comas. El programa
debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario
para traducirla palabra a palabra. Si una palabra no está en el
diccionario debe dejarla sin traducir."""

diccionario = {}

while True:
    print("1-añadir palabra al diccionario")
    print("2-diccionario")
    print("3-salir")
    o = input("Elige una opcion: ")
    if o =="1":
        palabra = input("Palabra a traducir [hola:hello]: ")
        palabras = palabra.split(":")
        diccionario[palabras[0]]=palabras[1]
    elif o == "2":
        plb=input(print("Introduce una palabra en castellano: "))
        for i  in range(len(diccionario)):
            if plb in diccionario:
                print(plb + "significa "+diccionario[plb])
        break
    else:
        print("opcion no valida")

"""Ejercicio 9
Escribir un programa que gestione las facturas pendientes de
cobro de una empresa. Las facturas se almacenarán en un
diccionario donde la clave de cada factura será el número de
factura y el valor el coste de la factura. El programa debe
preguntar al usuario si quiere añadir una nueva factura, pagar
una existente o terminar. Si desea añadir una nueva factura se
preguntará por el número de factura y su coste y se añadirá al
diccionario. Si se desea pagar una factura se preguntará por el
número de factura y se eliminará del diccionario. Después de
cada operación el programa debe mostrar por pantalla la
cantidad cobrada hasta el momento y la cantidad pendiente de
cobro."""

facturas = {}
facturas_pagadas = []
while True:
    print("1-Añadir fatura")
    print("2-pagar factura")
    print("3-salir")
    option = input("Elige una opcion: ")
    if option =="1":
        num_factura = input("Introduce el nuemero de factura: ")
        precio_factura = float(input("Introduce el coste de la factura: "))
        facturas[num_factura]=precio_factura
    if option =="2":
        print(facturas)
        o = input("Que factura quieres pagar? ")
        if o in facturas:
            facturas_pagadas.append(facturas[o])
            facturas.pop(o)
            print("Hasta la fecha has pagado: " ,sum(facturas_pagadas))
            print("Te queda por pagar: ",sum(facturas.values()))
        else:
            print("Factura no existente")
    if option =="3":
        break
    else:
        print("Opcion no valida")
            
"""Ejercicio 10
Escribir un programa que permita gestionar la base de datos
de clientes de una empresa. Los clientes se guardarán en un
diccionario en el que la clave de cada cliente será su NIF, y el
valor será otro diccionario con los datos del cliente (nombre,
dirección, teléfono, correo, preferente), donde preferente
tendrá el valor True si se trata de un cliente preferente. El
programa debe preguntar al usuario por una opción del
siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3)
Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes
preferentes, (6) Terminar. En función de la opción elegida el
programa tendrá que hacer lo siguiente:
1. Preguntar los datos del cliente, crear un diccionario con
los datos y añadirlo a la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la
base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su
NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos
con su NIF y nombre.
6. Terminar el programa."""

clientes = {}
datos = {}



while True:
    print("1-Añadir cliente")
    print("2-Eliminar cliente")
    print("3-Mostrar cliente")
    print("4-Todos los clientes")
    print("5-Clientes preferentes")
    print("6-Terminar")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        preferente = input("Preferente [si/no]: ")
        if preferente == "si":
            preferente = True
        elif preferente == "no":
            preferente = False
        else:
            preferente = False
        datos["nombre"]=nombre
        datos["direccion"]=direccion
        datos["telefono"]=telefono
        datos["correo"]=correo
        datos["preferente"]=preferente
        clientes[nif]=dict(datos)
        datos.clear()
    elif opcion == "2":
        print("Clientes actuales: ",clientes.keys())
        cliente = input("Cliente a eliminar: ")
        clientes.pop(cliente)
    elif opcion == "3":
        print("Clientes actuales: ",clientes.keys())
        cliente = input("Cliente a mostrar: ")
        print(clientes[cliente].items())
    elif opcion == "4":
        print(clientes.items())
    elif opcion == "5":
        for i in range(len(clientes)):
            if clientes[i][5] is True or False:
                print(clientes[i].keys())
    elif opcion == "6":
        break

"""Ejercicio 11
El directorio de los clientes de una empresa está organizado en
una cadena de texto como la de más abajo, donde cada línea
contiene la información del nombre, email, teléfono, nif, y el
descuento que se le aplica. Las líneas se separan con el
carácter de cambio de línea \n y la primera línea contiene los
nombres de los campos con la información contenida en el
directorio.
"nif;nombre;email;teléfono;descuento\n01234567L
;Luis
González;luisgonzalez@mail.com;656343576;12.5\n
71476342J;Macarena
Ramírez;macarena@mail.com;692839321;8\n63823376
M;Juan José
Martínez;juanjo@mail.com;664888233;5.2\n9837654
7F;Carmen
Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la
información del directorio, donde cada elemento corresponda a
un cliente y tenga por clave su nif y por valor otro diccionario
con el resto de la información del cliente. Los diccionarios con
la información de cada cliente tendrán como claves los
nombres de los campos y como valores la información de cada
cliente correspondientes a los campos. Es decir, un diccionario
como el siguiente
{'01234567L': {'nombre': 'Luis González',
'email': 'luisgonzalez@mail.com', 'teléfono':
'656343576', 'descuento': 12.5}, '71476342J':

{'nombre': 'Macarena Ramírez', 'email':
'macarena@mail.com', 'teléfono': '692839321',
'descuento': 8.0}, '63823376M': {'nombre':
'Juan José Martínez', 'email':
'juanjo@mail.com', 'teléfono': '664888233',
'descuento': 5.2}, '98376547F': {'nombre':
'Carmen Sánchez', 'email': 'carmen@mail.com',
'teléfono': '667677855', 'descuento': 15.7}}"""
                                 
informacion = "nif;nombre;email;teléfono;descuento\n01234567L;LuisGonzález;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamírez;macarena@mail.com;692839321;8\n63823376M;Juan JoséMartínez;juanjo@mail.com;664888233;5.2\n98376547F;CarmenSánchez;carmen@mail.com;667677855;15.7"

cliente = {}
datos = {}

info = informacion.split("\n")
campos = info[0].split(";")
del info[0]
lista_info = info.split(";")
for i in range(len(lista_info)):
    datos2 = i.split(";")
    for j in range(1,len(campos)):
        datos[campos[j]] = datos2[j]
    cliente[campos[0]]=datos
print(cliente)
        
        