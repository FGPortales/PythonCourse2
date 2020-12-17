import pickle


class Persona:
    personas = []

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def agregar_personas(self, p):
        self.personas.append(p)
        print(self.personas)
        self.agregar_fichero(self.personas)

    def agregar_fichero(self, personas):
        fichero = open('personas.pckl', 'wb')
        pickle.dump(personas, fichero)
        fichero.close()
        self.ver_fichero()

    def ver_fichero(self):
        fichero = open('personas.pckl', 'rb')
        personnitas = pickle.load(fichero)
        for p in personnitas:
            print(p)
        fichero.close()


if __name__ == '__main__':
    nombres = ['Pedro', 'Maria', 'Diego']
    for n in nombres:
        p = Persona(n)
        p.agregar_personas(p)

