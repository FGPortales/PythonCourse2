numeros = [2, 5, 10, 23, 50, 33]


def doblar(numero):
    return numero*2


m = map(doblar, numeros)

print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(list(m))

a = [1, 2, 3, 4, 5]
b = [7, 6, 5, 4, 3]

print(list(map(lambda x, y: x * y, a, b)))

c = [2, 2, 2, 2, 2, 2]
print(list(map(lambda x, y, z: x * y * z, a, b, c)))

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

personas = map(lambda persona: Persona(persona.nombre, persona.edad + 1), personas)
for p in personas:
    print(p)


