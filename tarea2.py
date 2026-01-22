print("Operaciones Basicas")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
opcion = input("Ingrese la opcion a realizar (1, 2, 3, 4): ")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if opcion == '1':
    resultado = num1 + num2
    print("La suma de {} y {} es: {}".format(num1, num2, resultado))
if opcion == '2':
    resultado = num1 - num2
    print("La resta de {} y {} es: {}".format(num1, num2, resultado))
if opcion == '3':
    resultado = num1 * num2
    print("La multiplicacion de {} y {} es: {}".format(num1, num2, resultado))
if opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("La division de {} y {} es: {}".format(num1, num2, resultado))
