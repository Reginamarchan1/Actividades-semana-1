num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce otro numero"))

if num1>num2:
    print(num1,"es mayor y", num2,"es menor")
elif num2>num1:
    print(num2, "es mayor y", num1, "es menor")
else:
    print(num1, "y", num2, "son iguales")

print("Fin.")             