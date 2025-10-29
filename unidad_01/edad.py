while True:
        edad = int(input("Introduce tu edad: "))

        if edad < 1 and edad > 120:
            print("Edad debe ser entre 1 y 120")
            continue
        if edad == 1 and edad == 15:
            print("Eres niño/a")
        elif edad == 16 and edad == 21:
            print("Eres adolescente")
        elif edad == 22 and edad == 35:
            print("Eres joven")
        elif edad == 36 and edad == 50:
            print("Eres maduro/a")
        elif edad == 51 and edad == 60:
            print("Eres de mediana edad")
        elif edad == 61 and edad == 80:
            print("Eres mayor")
        elif edad == 81 and edad == 100:
            print("Eres viejo/a")
        else:
            print("Eres centenario/a")
        break