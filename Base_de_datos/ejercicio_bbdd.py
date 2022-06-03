# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:28:59 2022

@author: Jun
"""
import pymysql

def database (query):
    try:
        conn=pymysql.connect(host = "localhost", port = 3308, user = "root", passwd = "", database = "ejercicio_bbdd")
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()
        for base in cursor:
            print(base)
        conn.close()
        
    except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error: ",e)

database("delete from agenda where nombre = 'qwe'")
database("update agenda set telefono = '66218723' where nombre = 'qwe'")
database("select * from agenda")
database("INSERT INTO agenda (nombre, telefono) VALUES ('asd', '7829361'), ('qwe', '2763817');")

def add_contact():
    nombre = input("Nombre del contacto: ")
    telf = input("Numero de contacto: ")
    query = f"insert into agenda (nombre,telefono) values ({nombre},{telf})"
    database(query)
    
def del_contact():
    
def update_contact():
    
def get_contact():
    
def menu():
    while True:
        print("AGENDA")
        print("------------------------")
        print("[1]-Mostrar contactos")
        print("[2]-Crear contacto")
        print("[3]-Eliminar contacto")
        print("[4]-Actualizar contacto")
        print("------------------------")
        o = int(input("Elige una opcion: "))
        
        if o == 1:
            get_contact()
        elif o == 2:
            add_contact()
        elif o == 3:
            del_contact()
        elif o == 4:
            update_contact()
        else:
            print("Opcion no valida")
menu()