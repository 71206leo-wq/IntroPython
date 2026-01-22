sueldo = float(input("Ingresa el sueldo de la persona: "))
impuesto = 0

if sueldo < 1000:
    impuesto = 0

if sueldo >= 1000 and sueldo <= 2000:
    impuesto = sueldo * 0.10

if sueldo > 2000:
    impuesto = sueldo * 0.20

sueldo_neto = sueldo - impuesto

print(f"Impuesto a pagar: ${impuesto:.2f}")
print(f"Sueldo neto después de impuesto: ${sueldo_neto:.2f}")
