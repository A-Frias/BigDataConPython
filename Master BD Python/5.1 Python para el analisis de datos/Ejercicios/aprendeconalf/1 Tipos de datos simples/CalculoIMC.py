peso=input("¿Cuanto pesas? ")
altura = input("¿Cuanto mides? ")
imc = int(peso) / float(altura) ** 2
print("Tu indice de masa corporal es: {}".format(imc))