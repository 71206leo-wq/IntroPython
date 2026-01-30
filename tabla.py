# Crear un programa que pida un mumero al usuario una ves ingresado imprimir la tabla de multiplicar de ese numero con un ciclo for 
 
num=int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print("Tabla de multiplicar del numero " + str(num) + ":")
for i in range(1,11):
        resultado=num*i
        print(str(num) + " x " + str(i) + " = " + str(resultado))
        