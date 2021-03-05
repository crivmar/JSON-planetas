from funciones import *

documento=leer_documento("/home/crivero/Descargas/Git/JSON-planetas/planets.json")

print(documento)

m=0
while m!=6:
    m=menu()
    ## Ejercicio 1##
    for i,j in listar_info(documento).items():
        print(" ")
        print(i,"y esta es su imagen:", j)