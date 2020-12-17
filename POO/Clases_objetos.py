class Pelicula:
    def __init__(self, titulo, duracion, lanzamineto):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamineto
        print("Se ha creado la pelicula ", self.titulo)

    def __del__(self):
        print("Se esta borrando la película", self.titulo)

    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    def __len__(self):
        return self.duracion


if __name__ == '__main__':
    p = Pelicula("El padrino", 175, 1972)
    print(len(p))
    print((str(p)))
