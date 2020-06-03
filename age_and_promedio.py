name = input("Introduce el nombre de la persona: ")

age = int(input("Introduce la edad de la persona: "))
promedio = float(input("Introduce tu promedio: "))


if age < 6: 
    print(name, "Está en maternal")
    print(name, "No calificas para esta área")
       
elif age >= 6 and age < 12:
    print(name, "Está en primaria")
        
    if promedio >= 9.5:
        print("Tu promedio es sobresaliente")
    else: 
         print("Debes mejorar tu rendimiento")

elif age >= 12 and age < 15:
    print(name, "Está en secundaria")
       
    if promedio >= 9:
        print("Tu promedio es sobresaliente")
    else: 
        print("Debes mejorar tu rendimiento")

elif age >= 15 and age < 18:
    print(name, "Está en preparatoria")
         
    if promedio >= 8.5:
        print("Tu promedio es sobresaliente")
    else: 
        print("Debes mejorar tu rendimiento")
elif age >= 18 and age < 23:
    print(name, "Está en universidad")
         
    if promedio >= 8:
            print("Tu promedio es sobresaliente")
    else: 
            print("Debes mejorar tu rendimiento")
else: 
    print(name, "Es profesional")
    print("Tú no estudias")

