

name = str(input('Introduce tu nombre: '))
last_name = str(input('Introduce tus apellidos: '))
age = int(input('Introduce tu edad: '))
email = str(input('Introduce tu email: '))

dic = {
    'nombre': name,
    'apellido': last_name, 
    'edad': age, 
    'email': email
    
}

print(f"Hola, mi nombre es: {dic['nombre']}{dic['apellido']}, tengo {dic['edad']} años y mi corre electrónico es: {dic['email']}")
