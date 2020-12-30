def main():
    """Funcines Generadoras"""
    # my_list = [numero for numero in [0, 1, 2, 3, 4, 5] if numero % 2 == 0]
    # print(my_list)
    # my_list = [numero for numero in range(0,6) if numero % 2 == 0]
    # print(my_list)
    def pares(n):
        for numero in range(n+1):
            if numero % 2 == 0:
                yield numero
    # value = pares(10)
    # print(value)
    # for numero in pares(10):
    #     print(numero)

    # CONVERTIR UNA LISTA EN ITERABLE o cadena
    lista = [1, 2, 3, 4, 5]
    cadena = "Hola Mundo"
    lista_iterable = iter(lista)
    cadena_iterable = iter(cadena)
    print(lista_iterable)  # Iterable
    print(cadena_iterable)  # Iterable



if __name__ == '__main__':
    main()
