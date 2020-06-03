for i in range(0,301):
    if i % 2 == 0: 
        print("Los números pares hasta 300 son: ", i)

for i in range(0,21):
    print("La tabla del multiplicación {}*15 es: {}".format(i,i*15) )
x = []
for i in range(50,101):
    if i % 2 != 0:
        x.append(i)
print("La súma de números impares de 50 a 100 es: ",sum(x))
    
lst=[]
for i in range(10,101):
    if i % 2 == 0:
        lst.append(i)
        
print("La suma de pares de 10 a 100 es: ",sum(lst))

    