
def main():
    # def hola():
    #     def bienvenido():
    #         return "Hola!"
    #
    #     return bienvenido
    # a = hola()
    # print(a)
    def hola():
        print("Hola!!")

    def adios():
        print("Adiós!!")

    def monitorizar(funcion):
        def decorar():
            print("\t *Se está apunto de ejecutar la función:", funcion.__name__)
            funcion()
            print("\t *Se ha finalizado la ejecución de la función:", funcion.__name__)

        return decorar

    # monitorizar(hola)()
    # monitorizar(adios)()

    def monitorizar_args(funcion):
        def decorar(*args, **kwargs):
            print("\t *Se está apunto de ejecutar la función:", funcion.__name__)

            funcion(*args, **kwargs)

            print("\t *Se ha finalizado la ejecución de la función:", funcion.__name__)

        return decorar

    @monitorizar_args
    def hola(nombre=None):
        print("Hola!, {}".format(nombre))

    @monitorizar_args
    def adios(nombre=None):
        print("Adiós!, {}".format(nombre))

    hola("sd")
    adios("Hector")


if __name__ == '__main__':
    main()
