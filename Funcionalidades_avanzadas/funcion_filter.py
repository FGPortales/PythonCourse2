# numeros = [2, 5, 10, 23, 50, 33]
#
#
# def multiple(numero):
#     if numero % 5 == 0:
#         return True
#
#
# print(list(filter(multiple, numeros)))
#
# f = filter(multiple, numeros)
# print(next(f))
# print(next(f))
#
# print(list(filter(lambda numero: numero % 5 == 0, numeros)))

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(menor)
