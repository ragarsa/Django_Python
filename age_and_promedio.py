name = input("Introduce el nombre de la persona: ")

age = int(input("Introduce la edad de la persona: "))


if age > 0:

    if age < 6: 
        print(name, "Está en maternal")
        print(name, ",no calificas para esta área")

       
    elif age >= 6 and age < 12:
        print(name, "Está en primaria")
        promedio = float(input("Introduce tu último promedio: "))
        if promedio >= 9.5:
            print("Tu promedio es sobresaliente")
        else: 
            print("Debes mejorar tu rendimiento")

    elif age >= 12 and age < 15:
        print(name, "Está en secundaria")
        promedio = float(input("Introduce tu último promedio: "))
        if promedio >= 9:
            print("Tu promedio es sobresaliente")
        else: 
            print("Debes mejorar tu rendimiento")

    elif age >= 15 and age < 18:
        print(name, "Está en preparatoria")
        promedio = float(input("Introduce tu último promedio: "))
        if promedio >= 8.5:
            print("Tu promedio es sobresaliente")
        else: 
            print("Debes mejorar tu rendimiento")
    elif age >= 18 and age < 23:
        print(name, "Está en universidad")
        promedio = float(input("Introduce tu último promedio: "))
        if promedio >= 8:
            print("Tu promedio es sobresaliente")
        else: 
            print("Debes mejorar tu rendimiento")
    else: 
        print(name, "Es profesional")
        print("Tú no estudias")
else: 
    print("Tú no has nacido o eres un bebé")
