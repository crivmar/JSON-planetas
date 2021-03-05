def leer_documento(d):
    import json
    with open(d) as f:
        l=json.load(f)
    return l

def menu():
    print('''
    1. Nombre e imagenes de los planetas del Sistema Solar.
    2. Nº de satélites por planeta.
    3. Satélites de un planeta.
    4. Búsqueda de planeta por su satélite.
    5. Distancia de los planetas al Sol.
    6. Salir
    ''')
    opcion=int(input("Elige una opción: "))
    print("-"*40)
    while opcion<1 or opcion>6:
        print("Error")
        opcion=int(input("Elige una opción: "))
    return opcion

def listar_info(l):
    dic={}
    for i in l:
        dic[i.get("name")]=i.get("image")
    return dic
