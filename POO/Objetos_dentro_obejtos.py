class Pelicula:

    def __init__(self, titulo, duracion, lanzamineto):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamineto
        print("Se ha creado la pelicula ", self.titulo)

    def __str__(self):
        return "{} ({})".format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)


if __name__ == '__main__':
    p = Pelicula("El padrino", 175, 1972)
    c = Catalogo([p])
    c.mostrar()
    c.agregar(Pelicula("El hombre araña", 202, 1974))
    c.mostrar()
