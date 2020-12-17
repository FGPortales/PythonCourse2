from io import open  # esto en caso si se trabaja en un script
import pickle


class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)  # agrgamos las peliculas en una lista
        self.guardar()  # se va guardando

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo esta vacio")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} peliculas".format(len(self.peliculas)))

    def guardar(self):
        print("Estoy en guardar")
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()

    # Destructor de clase

    def __del__(self):
        self.guardar()  # Guardado automático
        print("Se ha guardado el fichero")

if __name__ == '__main__':
    c = Catalogo()
    # c.mostrar()
    c.agregar(Pelicula("El padrino", 174, 1972))
    c.agregar(Pelicula("El padrino: parte 2", 202, 1974))
    c.mostrar()
