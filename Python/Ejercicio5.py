precio = float(input("Introduce el precio de un producto: "))
p_descuento = int(input("Introduce el porcentaje: "))

paga = precio - (precio * p_descuento /100)

print(f"El precio final es ${paga}")

print("Fin.")