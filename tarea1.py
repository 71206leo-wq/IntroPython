edad1 = int(input("Ingrese la edad de la persona 1: "))
edad2 = int(input("Ingrese la edad de la persona 2: "))

if (edad1 > edad2):
 print("La persona 1 es mayor que la persona 2.)".format(edad1, edad2))
else:
    if (edad2 > edad1):   
        print("La persona 2 es mayor que la persona 1.".format(edad2, edad1))
    else:
        print("Ambas personas tienen la misma edad: {}.".format(edad1, edad2))
