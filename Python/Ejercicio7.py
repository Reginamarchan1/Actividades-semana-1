peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))

imc = peso/(altura**2)

print("Su imc es", round(imc, 2))

print("Fin.")