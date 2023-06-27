import msvcrt
import numpy as np
import os
from colorama import Fore, Style
import random

columna=7
filas=10
registro = np.empty([7,10], object)
anotaciones= ["Anotación positiva: el alumno aporta a la clase y demuestra un buen desempeño","Anotación negativa: el alumno se niega a cooperar con sus compañeros de clase","Anotación negativa: el alumno se niega a salir de clases y comienza a golpear las mesas de sus compañeros", "Anotación positiva: el alumno realiza todas las tareas semanales"]
notas=["7.0","5.1","3.2","4.7","1.0","6.5"]
#funcion para limpiar pantalla

def limpiarpan():
    print("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system('cls')

#funcion para desplegar un menu 

def menu():
    print("""SISTEMA DE REGISTRO ALUMNOS 
    COLEGIO SAN CHARLIS
    ---------------------------
    1) Registrar alumno
    2) Buscar alumno
    3) Imprimir certificado
    4) Salir
    """)
    opcion=int(input("Seleccione : "))
    while opcion>4 or opcion<1:
        opcion=int(input("Opcion invalida. Seleccione nuevamente : "))
    return opcion
def validaropc():
    opcion=int(input("Seleccione : "))
    while opcion>4 or opcion<1:
        opcion=int(input("Opcion no valida. Seleccione nuevamente : "))
    return opcion
#funcion para seleccionar las opciones del menu

def opcionesmenu(opcion):
    if opcion==1:
        print("Ha selecciona la opcion de registrar alumno")
        vesp=validarespacio(registro)
        if vesp==True:
            guardaralumno(registro)
    if opcion==2:
        print("Ha seleccionado la opcion de buscar alumno")
        rut=input("Ingrese el rut del alumno : ")
        buscaralumno(rut,registro)
    if opcion==3:
        print("Ha seleccionado la opcion de imprimir certificado")
        imprimircertificado(rut,registro)
    if opcion==4:
        print("Ha seleccionado salir del sistema")
        return False

#funcion para validar que haya espacio en el registro

def validarespacio(lista):
    if None in lista:
        return True
    else:
        return False
#Funcion para guardar un alumno en el registro

def guardaralumno(registro):
    for x in range(10):
        for y in range(7):
            if y==None:
                rut=input("Ingrese rut del alumno : ")
                vrut=validarrut(rut)
                if vrut==True:
                    registro[y]=rut
                else:
                    print("El rut ya se encuentra registrado en el sistema")
                nombre=input("Ingrese nombre completo del alumno : ")
                if validarnombre==True:
                    registro[y+1]=nombre
                else:
                    print("El nombre no posee entre 2 y 30 caracteres")
                edad=int(input("Ingrese la edad del alumno : "))
                if validaredad==True:
                    registro[y+2]=edad
                else:
                    print("La edad ingresada no es valida")
                genero=input("Ingrese el genero del alumno (M o F) : ").upper
                registro[y+3]=genero
                prom=int(input("Ingrese el promedio del alumno : "))
                registro[y+4]=prom
                fechamat=input("Ingrese la fecha de la matricula (dia/mes/año) : ")
                registro[y+5]=fechamat
                nomapod=input("Ingrese el nombre del apoderado : ")
                registro[y+6]=nomapod
                return True


#funcion para validar que el rut no se encuentre repetido

def validarrut(rut,lista):
    if rut in lista:
        return True
    else:
        return False

#funcion para validar que el nombre del alumno posea entre 2 y 30 caracteres 

def validarnombre(nombre):
    if len(nombre)<30 or len(nombre)>2:
        return True
    else:
        return False

#funcion para validar que la edad del alumno sea mayor a 4 años

def validaredad(edad):
    if edad>4:
        print("Edad valida")
        return True
    else:
        print("Edad no valida")
        return False

#funcion para buscar a un alumno por su rut

def buscaralumno(rut,lista):
    for x in range(columna):
        for y in range(filas):
            if rut in lista:
                pass
            else:
                pass

#funcion para imprimir certificados

def imprimircertificado(rut,lista):
    for x in range(filas):
        for y in range(columna):
            if rut in lista:
                print("""1)Anotaciones del alumno
                2) Certificado de notas
                3) Certificado de alumno regular
                """)
                opt=int(input("Seleccione : "))
                while opt>3 or opt<1:
                    opt=int(input("Opcion no valida. Seleccione nuevamente : "))
                if opt==1:
                    print("Ha selecciona la opcion 1)Anotaciones del alumno")
                    print(random.choice(anotaciones))
                    print(random.choice(anotaciones))
                    print(random.choice(anotaciones))
                elif opt==2:
                    print("Ha selecciona la opcion 2)Certificado de notas")
                    print(random.choice(notas))
                    print(random.choice(notas))
                    print(random.choice(notas))
                elif opt==3:
                    print("Ha selecciona la opcion 3)Certificado de alumno regular")
                    print(f"""Certificado de alumno regular
                    Rut: {y}
                    Nombre alumno: {y+1}
                    """)


                
            

