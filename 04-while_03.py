import os
op=0

while op!=5:
    os.system("cls")
    print("1.- suma\n2.-resta\n3.- multiplicacion\n4.- division\n5.- salir")
    op=int(input("Seleccciona una opcion del 1-5: "))
    if op==1:
        num1=int(input("Ingresa el primer numero: "))
        num2=int(input("Ingresa el segundo numero"))
        print("La suma de {} + {} es: {}".format(num1,num2,num1+num2))
        input("Presiona Enter para continuar...")
    if op==2:
        num1=int(input("Ingresa el primer numero: "))
        num2=int(input("Ingresa el segundo numero"))
        print("La resta de {} - {} es: {}".format(num1,num2,num1-num2))
        input("Presiona Enter para continuar...")
    if op==3:
        num1=int(input("Ingresa el primer numero: "))
        num2=int(input("Ingresa el segundo numero"))
        print("La multiplicacion de {} * {} es: {}".format(num1,num2,num1*num2))
        input("Presiona Enter para continuar...")
    if op==4:
        num1=int(input("Ingresa el primer numero: "))
        num2=int(input("Ingresa el segundo numero"))
        print("La division de {} / {} es: {}".format(num1,num2,num1/num2))
    else:
        print("Error: No se puede dividir entre cero.")
        input("Presiona Enter para continuar")
    
