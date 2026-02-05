import os

os.system("cls")

print("---------------Calificaciones---------------")

calificacion = int(input("\nIngresa la calificacion de la persona: "))
if calificacion>=7:
    if calificacion >=9:
        print("\nExcelente")
    else:
        print("\nAprobado")
else:
    print("\nReprobado")


