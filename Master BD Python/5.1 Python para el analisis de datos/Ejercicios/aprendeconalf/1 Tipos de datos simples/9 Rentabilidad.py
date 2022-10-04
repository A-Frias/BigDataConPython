from unicodedata import digit


capital=input("Introduce el capital inicial: ")
interes=input("Introduce el interes anual: ")
años=input("Introduce el numero de años: ")
capital=float(capital)
interes=float(interes)
años=int(años)
for i in range(años):
    capital=round(capital*(1+interes/100),2)
    print("Capital tras el año {}: {}".format(i+1, capital))
