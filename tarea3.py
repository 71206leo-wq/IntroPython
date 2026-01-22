
print("\nFiguras Geometricas")
print("1. Triangulo")
print("2. Cuadrado")
print("3. Circulo")
print("4. Pentagono")
print("5. Salir")

opcion = input("Ingrese la opcion a realizar (1-5): ")

if opcion == '1':
        print("Figura seleccionada: TRIANGULO")
        base = float(input("Ingrese la base {}: "))
        altura = float(input("Ingrese la altura {}: "))
        area = (base * altura) / 2
        print("El area del triangulo es {}:", area)

if opcion =='2':
        print("Figura seleccionada: CUADRADO")
        lado1 = float(input("Ingrese el lado1 {}: "))
        lado2 = float(input("Ingrese el lado2 {}: "))
        area = lado1 * lado2
        print("El area del cuadrado es {}:", area)

if opcion == '3':
        print("Figura seleccionada: CIRCULO")
        radio = float(input("Ingrese el radio {}: "))
        area = 3.1416 * radio * radio
        print("El area del circulo es {}:", area)

if opcion == '4':
        print("Figura seleccionada: PENTAGONO")
        lado = float(input("Ingrese el lado {}: "))
        apotema = float(input("Ingrese el apotema {}: "))
        area = (5 * lado * apotema) / 2
        print("El area del pentagono es {}:", area)

if opcion =='5':
        print("Saliendo del programa...")
