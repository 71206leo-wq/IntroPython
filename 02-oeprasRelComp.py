import math, os


os.system("cls")


print("----Grupos ICO201-9, ICO201-14----")


num1= input("Ingrese el primer numero:")
num2= input("Ingrese el segundo numero: ")

suma=int(num1) + int(num2)
print("La suma de {} con {} es:{}".format(num1,num2, suma))

resta=int(num1) - int(num2)
print("La resta de {} con {} es:{}".format(num1,num2, resta))

multiplicacion=int(num1) * int(num2)
print("La multiplicacion de {} con {} es:{}".format(num1,num2, multiplicacion))

division=int(num1) / int(num2)
print("La division de {} con {} es:{}".format(num1,num2, division))

potencia=int(num1) ** int(num2)
print("La potencia de {} con {} es:{}".format(num1,num2, potencia))

print("Operaciones basicas"\n1,- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n")
      
opcion=input("Ingrese la opcion a realizar(1,,2,3,4);")


val1=5
val2=3

temp=val1>val2 #False
temp=val1==val2 #False
temp=val1<val2 #True
temp=val1>=val2 #False
temp=val1!=val2 #True

print("El valor de la comparacion es: ";, temp)

tem2= not(val1>val2) and (val1<val2) #True
print("El valor de la comparacion con NOT y and es: ", tem2)



