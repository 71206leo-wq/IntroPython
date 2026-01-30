# Crear uh programa que le pida al usuario un numero y el programa debera imprimir la piramide de asteriscos segun el numero ingresado
num=int(input("Ingrese un numero para imprimir la piramide de asteriscos: "))
for i in range(1,num+1):
    print("*"*i)
    