import funcionesp3 as funp
#Opcion 1. Registrar: Corresponde a guardar ciertos datos de un alumno, entre ellos: 
#Rut, nombre completo, edad, género, promedio de notas, fecha matricula y nombre del apoderado.
#Además, debe verificar que el rut no se encuentre repetido, el nombre del alumno considere entre 2 y 30 caracteres
#y la edad sea mayor o igual a 4 años.

#Opción 2
#Buscar: Corresponde buscar un alumno por su rut y mostrar toda su información almacenada.

#Opción 3
#Imprimir certificados: Esta opción permite imprimir los certificados de 1) anotaciones de un alumno, 
#2) certificado de notas y 3) certificado de alumno regular. 
#Estos certificados deben ser previamente ingresados con valores aleatorios. 
#Al imprimir el certificado, debe mostrar el nombre del certificado, rut y nombre del alumno.

#Opción 4 
#Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y la versión del programa.

while True:
    funp.limpiarpan()
    print("""SISTEMA DE REGISTRO ALUMNOS 
        COLEGIO SAN CHARLIS
        ---------------------------
        1) Registrar alumno
        2) Buscar alumno
        3) Imprimir certificado
        4) Salir
        """)
    opcion=funp.validaropc()
    if opcion==False:
        break
    funp.opcionesmenu(opcion)


    

    

