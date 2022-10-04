import random
from re import I
def suma_acumulada(lista, n=0):
    
    if n==(len(lista)-1):
        
        return lista
        
    else:
        lista[n+1] = lista[n] + lista[n+1]
   
        return suma_acumulada(lista, (n+1))
        


def marinero_borracho(n):
    pasos=random.choices([-1,1], k=n)
    pos=[0]+suma_acumulada(pasos)
    return pos
#print(marinero_borracho(10))

import itertools as it

def marinero_borracho2(n):
    pasos = ( random.choice([-1,1]) for i in range(n) )
    pos= it.accumulate(pasos)
    return pos

print(list(marinero_borracho2(10)))

import seaborn as sns
import matplotlib.pyplot as plt

def grafica_marinero_borracho(n, intentos):
    for i in range(intentos):
        pos= marinero_borracho(n)
        sns.lineplot(x=range(n+1), y=pos)
    plt.show()


def grafica_marinero_borracho2(n, intentos):
    pos = [marinero_borracho(n) for i in range(intentos)]
    for i in pos:
        sns.lineplot(x=range(n+1), y=i)
    plt.show()

grafica_marinero_borracho2(1000, 10)



