from funciones import *

documento=leer_documento("/home/crivero/Descargas/Git/JSON-planetas/planets.json")

m=0
while m!=6:
    m=menu()
    ## Ejercicio 1 ##
    if m==1:
        for i,j in listar_info(documento).items():
            print(" ")
            print(i,"y esta es su imagen:", j)
    ## Ejercicio 2 ##
    if m==2:
        for i,j in cont_info(documento).items():
            print(" ")
            print(i,"tiene:",len(j),"lunas.")
