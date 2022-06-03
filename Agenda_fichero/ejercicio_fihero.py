# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:06:14 2022

@author: Jun
"""

"""Ejercicio 6
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes
de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para
consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un
cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su
teléfono deben aparecer separados por comas y cada cliente en una línea distinta."""

directorio = "D:/AA_Curso_Python/Python/Ejercicios_Phyton/Agenda_fichero/agenda.txt"

def agenda_txt():
    try: 
        file = open(directorio, "r")
    except FileNotFoundError:
        print(directorio + " no existe")
    else:
        agenda = file.readlines()
        file.close()
        agenda = dict([tuple(line.split(",")) for line in agenda])
        return agenda

def consultar():
    nombre = input("Nombre del contacto: ")
    agenda = agenda_txt()
    if nombre in agenda:
        print("El numero de "+ nombre + " es " + agenda[nombre])
        return
    else:
        print(nombre + " no esta en la agenda")
        return
    
def add_telefono():
    nombre = input("Nombre del contacto: ")
    agenda = agenda_txt()
    if nombre in agenda:
        print("Contacto existente")
        return
    else:
        telefono = input("Telefono: ")
        file = open(directorio,"a")
        file.write(nombre + "," + telefono + "\n")
        file.close()
        print("Contacto añadido correctamente")
        return
        
def delete_telefono():
    name = input("Nombre del contacto: ")
    agenda = agenda_txt()
    if name in agenda:
        del agenda[name]
        file = open(directorio, "w")
        for nombre, telefono in agenda.items():
            file.write(nombre + "," + telefono)
        print(name + " ha sido eliminado")
        file.close()
    else:
        print(name + " no existe")
    
def mostrar():
    agenda = agenda_txt()
    contactos = agenda.items()
    contador = 1
    for nombre,telefono in contactos:
        print("[",contador,"] - " , nombre + " - " + telefono)
        contador += 1
    return

def menu ():
    while True:
        print("Agenda")
        print("-------------------------")
        print("[0]-Mostrar agenda")
        print("[1]-Consultar")
        print("[2]-Añadir telefono")
        print("[3]-Eliminar telefono")
        print("[4]-Salir")
        print("-------------------------")
        option = int(input("Opcion: "))
        
        if option == 0:
            mostrar()
        elif option == 1:
            consultar()
        elif option == 2:
            add_telefono()
        elif option == 3:
            delete_telefono()
        elif option == 4:
            break
        else:
            print("Opcion no valida")
menu()