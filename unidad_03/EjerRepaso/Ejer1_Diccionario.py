diccionario = [{"nombre": "Manu", "edad": 21, "estudiante": True},
               {"nombre": "Alex", "edad": 51, "estudiante": False},
               {"nombre": "Fran", "edad": 24, "estudiante": True}]

for persona in diccionario:
    if persona["edad"] <= 18 :
        print(f"{persona['nombre']} es menor de edad")
    elif persona["edad"] >= 18 and persona["edad"] <= 25:
        print(f"{persona['nombre']} es muy joven")
    elif persona["edad"] >= 26 and persona["edad"] <= 40:
        print(f"{persona['nombre']} es joven")
    elif persona["edad"] >= 41:
        print(f"{persona['nombre']} ya no es joven")
