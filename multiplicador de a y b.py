# Crear un programa que me permita realizar la multiplicacion de a y b sin utilizar el operador de multiplicacion usar el operador de suma y un ciclo while para pedir dos numeros
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
resultado=0
cont=0
while cont<b:
    resultado=resultado+a
    cont=cont+1
print("El resultado de la multiplicacion de " + str() + " y " + str() + " es: " .format(a,b,resultado))
