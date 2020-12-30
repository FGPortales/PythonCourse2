"""Generadores: Permiten extraer valores de una función y almacenarlo
(de uno en uno) en objetos iterables (que se pueden recorrer),
sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM"""

"""
def genera_multiplos7(limite):
    numero = 1
    lista_numeros = []

    while numero <= limite:
        lista_numeros.append(numero * 7)
        numero = numero + 1
    return lista_numeros


print(genera_multiplos7(10))
"""


def generador_multiplos7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7
        numero += 1


obtiene_multiplo7 = generador_multiplos7(10)
# print(obtiene_multiplo7)
#
# for n in obtiene_multiplo7:
#     print(n)

# next(): Retorna el siguiente elemento de un objeto iterable:
print(next(obtiene_multiplo7))
print("Acá 100")
print(next(obtiene_multiplo7))
print("Acá 300")
print(next(obtiene_multiplo7))


"""
        LOS GENERADORES
- Son más eficiente que las funciones tradicionales
- Muy útiles con listas de valores infinitos.
- Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).

"""
