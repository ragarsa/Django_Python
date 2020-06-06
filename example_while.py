print("BIENVENIDO A LA CALCULADORA DE SALARIOS")


selection = 'Si'

while selection == 'Si': 
    name = input("Introduce tu nombre completo: ")
    salary_compl = float(input("Introduce tu salario: "))
    salary_iva = salary_compl * 0.84
    print("El salario bruto de", name, 'es de:', salary_iva)
    selection = input("¿Desea ingresar otro salario (Si/No)? " )

else: 
    print("Hasta luego")
