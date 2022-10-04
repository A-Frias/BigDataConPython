asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
msje = "Yo estudio {}"
msje = [msje] + [", {}" for i in range(len(asignaturas)-2)]
msje = msje + [" y {}"]

#msje = "".join(msje)
import functools
msje= functools.reduce(lambda a, b: a+b, msje)
print(msje)
print(asignaturas)
print(*asignaturas)
print(msje.format(*asignaturas))