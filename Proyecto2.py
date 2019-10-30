import re

class Reader ():

    def readerPalabras(self, archivo):
        with open(archivo) as fp:
            arreglo = [word for line in fp for word in line.split()]
        return arreglo

    def reader(self, archivo):
        with open(archivo) as fp:
            arreglo = [line for line in fp]
        return arreglo

    def splitter(self, cadena):
        cadena = cadena.split("(")[0]
        cadena = cadena.split(")")[0]
        cadena = cadena.split(",")[0]
        cadena = cadena.split(".")[0]
        cadena = cadena.split("<")[0]
        cadena = cadena.split("[")[0]
        cadena = cadena.split("{")[0]
        return cadena

lector = Reader()
temporal = input("Inserta el archivo: ")
contador1 = 1
contador2 = 2
contadorVariables = 0
contadorLineas = 0
archivo = lector.readerPalabras(temporal)
archivo2 = lector.reader(temporal)
print("Variables que no cunplen con el estandar")
for i in archivo:
    if (i == "String" or i == "byte" or i == "int" or i == "float" 
    or i == "double" or i == "char" or i == "boolean" or i == "void" or i == "new"
    or i == "class"):
        cadena = archivo[contador1]
        cadena = lector.splitter(cadena)
        print(cadena,len(cadena))
        if len(cadena) < 3:
            print(cadena)
            contadorVariables = contadorVariables + 1
    contador1 = contador1 + 1

print("")
print("Lineas extensas que no cumplen con el estandar")
for i in archivo2:
    caracteres = len(i.strip())
    if(caracteres > 100):
        print(i.strip())
        contadorLineas = contadorLineas + 1
    cibtadir2 = contador2+2

print("")
print ("La cantidad de nombres de variables cortas no descriptivas que se encontraron son: ",contadorVariables)
print ("La cantidad de lineas que exceden el estandar de longitud 100 es: ", contadorLineas)
print ("Total de variables encontradas: ", contador1-1)
print ("Total de lineas encontradas: ", contador2-2)
#(
#.
#,
#<
        