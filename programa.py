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
            if i=="Mercurio":
                print("Mercurio no tiene lunas.")
            elif i=="Venus":
                print("Venus no tiene lunas.")
            elif i=="Tierra":
                print(i,"tiene",len(j),"luna.")
            else:
               print(i,"tiene",len(j),"lunas.") 
    ## Ejercicio 3 ##
    if m==3:
        print(" ")
        print(filtro(documento))
    ## Ejercicio 4 ##
    if m==4:
        print(" ")
        print(busc_rel(documento)) 
    ## Ejercicio 5 ##
    if m==5:
        for i,j in dist(documento).items():
            print(" ")
            print("La distancia de %s al Sol es de: %.2f millones de km." % (i,(j*149.6)))
            print("La luz tarda aproximadamente %i minutos en llegar." % ((j*149.6)/0.3//60))
print("Fin del programa.")
