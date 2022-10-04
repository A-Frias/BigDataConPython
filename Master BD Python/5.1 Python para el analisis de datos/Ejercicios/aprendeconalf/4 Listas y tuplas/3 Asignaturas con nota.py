from ctypes import sizeof


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
msje = "Introduce las notas por orden de {}"
msje = [msje] + [", {}" for i in range(len(asignaturas)-2)]
msje = msje + [" y {}"]
msje = "".join(msje)
notas = input(msje.format(*asignaturas))
notas = notas.split(",")
notas = [float(i) for i in notas]

#Creo una malla con asignaturas y notas
#malla = [(a,n) for a in asignaturas for n in notas)]
#print(malla)
#print(list(zip(asignaturas, notas)))
notas: dict = dict(zip(asignaturas, notas))
#print(notas)
msje2="La nota de {} es {}"
msje2 = [msje2] + [", de {} es {}" for i in range(len(asignaturas)-2)]
msje2 = msje2 + [" y de {} es {}"]
msje2 = "".join(msje2)

#print([ i for j in notas.items() for i in j])

print(msje2.format(*[ i for j in notas.items() for i in j]))


