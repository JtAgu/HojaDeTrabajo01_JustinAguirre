#ejercicio1
print("Ejercicio #1")
n=int(input("Ingrese un numero entero: "))
for i in range(n):
    for j in range (i+1):
        print("*",end="")
    print("")

print("======================")
#ejercicio2
print("Ejercicio #2")
c=0
n=int(input("Ingrese un numero entero mayor a 2: "))
for i in range(1,n):
    if n%i==0:
        c+=1
if c>2:
    print(str(n)+" No es un numero primo")
else:
    print(str(n)+" Es un numero primo")
