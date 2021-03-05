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
        if i.get("name")=="Mercury":
            dic["Mercurio"]=i.get("image")
        elif i.get("name")=="Earth":
            dic["Tierra"]=i.get("image")
        elif i.get("name")=="Mars":
            dic["Marte"]=i.get("image")
        elif i.get("name")=="Jupiter":
            dic["Júpiter"]=i.get("image")
        elif i.get("name")=="Saturn":
            dic["Saturno"]=i.get("image")
        elif i.get("name")=="Uranus":
            dic["Urano"]=i.get("image")
        elif i.get("name")=="Neptune":
            dic["Neptuno"]=i.get("image")
        elif i.get("name")=="Pluto":
            dic["Plutón"]=i.get("image")
    return dic

def cont_info(l):
    dic={}
    for i in l:
        if i.get("name")=="Mercury":
            dic["Mercurio"]="0"
        elif i.get("name")=="Venus":
            dic["Venus"]="0"
        elif i.get("name")=="Earth":                
            dic["Tierra"]=i.get("moons")
        elif i.get("name")=="Mars":
            dic["Marte"]=i.get("moons")
        elif i.get("name")=="Jupiter":
            dic["Júpiter"]=i.get("moons")
        elif i.get("name")=="Saturn":
            dic["Saturno"]=i.get("moons")
        elif i.get("name")=="Uranus":
            dic["Urano"]=i.get("moons")
        elif i.get("name")=="Neptune":
            dic["Neptuno"]=i.get("moons")
        elif i.get("name")=="Pluto":
            dic["Plutón"]=i.get("moons")
        else:
            dic[i.get("name")]=i.get("moons")
    return dic

def filtro(l):
    dic={}
    dicaux={}
    for i in l:
        if i.get("name")=="Mercury":
            dic["mercurio"]="No tiene lunas."
        elif i.get("name")=="Venus":
            dic["venus"]="No tiene lunas."
        elif i.get("name")=="Earth":                
            dic["tierra"]="La Luna"
        elif i.get("name")=="Mars":
            dic["marte"]=i.get("moons")
        elif i.get("name")=="Jupiter":
            dic["júpiter"]=i.get("moons")
        elif i.get("name")=="Saturn":
            dic["saturno"]=i.get("moons")
        elif i.get("name")=="Uranus":
            dic["urano"]=i.get("moons")
        elif i.get("name")=="Neptune":
            dic["neptuno"]=i.get("moons")
        elif i.get("name")=="Pluto":
            dic["plutón"]=i.get("moons")
        else:
            dic[i.get("name")]=i.get("moons")
    t=input("Introduce el nombre de un planeta, en español: ")
    t=t.lower()
    if t in dic:
        dicaux=dic[t]
    else:
        dicaux="Error."
    return dicaux
        
    

    