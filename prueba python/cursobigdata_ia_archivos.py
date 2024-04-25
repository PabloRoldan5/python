import sys
#ARCHIVOS

ejemplo1 = "Ejemplo1.txt"

archivo1 = open(ejemplo1,"r") #ANTES DE LEER UN ARCHIVO TENEMOS QUE ABRIRLO
archivo1.encoding.encode("utf-8")
print(archivo1.name)
print(archivo1.encoding)

#SI LEEMOS EL ARCHIVO EL PUNTERO SI SITUARA EN LA ULTIMA LINEA Y NO MUESTRA NADA PARA ELLO HAY QUE CERRAR Y VOLVER A ABRIR
archivo1.close()
archivo1 = open(ejemplo1,"r")

print(archivo1.read())

#GUARDAMOS LO DEL ARCHIVO EN UNA VARIABLE
archivo1.close()
archivo1 = open(ejemplo1,"r")
contenido = archivo1.read()
archivo1.close()
print("================")
print(contenido)
print("================")

#ABRIMOS EL ARCHIVO CON "WITH" PARA QUE SE CIERRE AUTOMATICAMENTE TRAS LEERLO
with open(ejemplo1,"r") as archivo1:
    print("================")
    contenido = archivo1.read()
    print(contenido)
    print("================")
print(archivo1.closed)
print("================")

#LEER LOS PRIMEROS 20 CARACTERES
with open(ejemplo1,"r") as archivo1:
    print("================")
    contenido = archivo1.read(20)
    print(contenido)
    print("================")
#VARIAS OPERACIONES DE LECTURA PARA VER QUE EL PUNTERO SE DESPLAZA
with open(ejemplo1,"r") as archivo1:
    print("================")
    print(archivo1.read(5))#LEO LOS 5 PRIMEROS CARACTERES
    print(archivo1.read(5))#LEO LOS SIGUIENTES 5 CARACTERES
    print(archivo1.read(8))#LEO LOS SIGUIENTES 8 CARACTERES
    print("================")
#VAMOS A LEER LINEA A LINEA
with open(ejemplo1,"r") as archivo1:
    print("================")
    linea1 = archivo1.readline()
    linea2 = archivo1.readline()
    print("Primera linea: " + linea1)
    print("Segunda linea: " + linea2)
    print("================")
#VAMOS A ALMACENAR LAS LINEAS EN UNA LISTA
with open(ejemplo1,"r") as archivo1:
    print("================")
    listaLineas = archivo1.readlines()
    print(listaLineas)
    print("Primera linea: " + listaLineas[0])
    print("Segunda linea: " + listaLineas[1])
    print("================")

#ESCRITURA DE ARCHIVOS
ejemplo1 = "Ejemplo1.txt"

with open(ejemplo1,"w") as archivo1:
    archivo1.write("Esta es una nueva linea\n")
    archivo1.write("Esta es una nueva linea")

#ESCRIBIR MULTIPLES LINEAS EN UN ARCHIVO
listaLineas = ["Linea 1\n","Linea 2\n","Linea 3"]
with open(ejemplo1,"w") as archivo1:
    for linea in listaLineas:
     archivo1.write(linea)

#VAMOS A AÑADIR LINEAS AL ARCHIVO EXISTENTE
with open(ejemplo1,"a") as archivo1:
     archivo1.write("Linea 1 añadida\n")
     archivo1.write("Linea 2 añadida\n")
     
#COPIAR UN ARCHIVO A OTRO ARCHIVO
with open(ejemplo1,"r") as archivo1:
    with open("Ejemplo2.txt","w") as archivo2:
        for linea in archivo1:
            archivo2.write(linea)