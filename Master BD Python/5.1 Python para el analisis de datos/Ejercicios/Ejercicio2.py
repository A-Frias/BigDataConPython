texto = """Y el Cuervo nunca emprendió el vuelo.
Aún sigue posado, aún sigue posado
en el pálido busto de Palas.
en el dintel de la puerta de mi cuarto.
Y sus ojos tienen la apariencia
de los de un demonio que está soñando.
Y la luz de la lámpara que sobre él se derrama
tiende en el suelo su sombra. Y mi alma,
del fondo de esa sombra que flota sobre el suelo,
no podrá liberarse. ¡Nunca más!"""


#import functools as ft
#def limpia_palabra(palabra):
#    if len(palabra) == 0:
#        return palabra
#    else:
#        arbalap = [palabra[i] for i in range(len(palabra)) if palabra[i].isalpha()]
#        return ft.reduce(lambda x,y: x+y , arbalap) 
#
#def limpia_texto(tx):
#    palabras = tx.split()
#    son_buenas = [palabra.isalpha() for palabra in palabras]
#    #palabras_malas = [palabra for palabra in palabras[not son_buenas]]
#    return ()
#
#print(limpia_texto("Hola, ¿como estas?"))

def limpia_palabra(tx: str) -> str:
    tx_list= [x for x in tx if x.isalpha()]
    return "".join(tx_list)
    
def limpia_texto(tx: str) -> list:
    palabras = tx.split()
    palabras_limpias = [limpia_palabra(palabra) for palabra in palabras]
    return palabras_limpias

def cuenta_elementos(lst:list) -> dict:
    dic = {}
    for elemento in lst:
        if elemento in dic:
            dic[elemento] += 1
        else:
            dic[elemento] = 1
    return dic

def ejercicio2(tx: str) -> dict:
    palabras = [palabra.lower() for palabra in limpia_texto(tx)]
    conteo2 = { p : palabras.count(p) for p in palabras}  
    print(conteo2)

    dic = cuenta_elementos(palabras)
    return dic

import collections as cl
def con_collections(tx: str) -> dict:
    palabras = [palabra.lower() for palabra in limpia_texto(tx)]
    dic = cl.Counter(palabras)
    return dic

#print(ejercicio2(texto))
print(dict(con_collections(texto)))
