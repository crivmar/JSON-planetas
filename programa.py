from funciones import *

documento=leer_documento("/home/crivero/Descargas/Git/JSON-planetas/planets.json")

print(documento)

m=0
while m!=6:
    m=menu()
    ## Ejercicio 1##
    print(listar_info(documento))