def main():
    # texto = "Una linea con texto\nOtra linea contexto"
    # fichero = open('fichero.txt', 'w')
    # fichero.write(texto)
    # fichero.close()

    # COMANDO DE LECTURA
    # fichero = open('fichero.txt', 'r')
    # texto = fichero.read()
    # fichero.close()
    # print(texto)

    # LECTURA POR LINEAS
    # fichero = open('fichero.txt')
    # lineas = fichero.readlines()
    # fichero.close()
    # print(lineas[:])

    # MODO DE EXTENSIÓN (MODO APPEND)
    # fichero = open('fichero.txt', 'a')
    # fichero.write('\nCuarta linea del fichero')
    # fichero.close()

    # MODO LECTURA PARA LEER LINEA POR LINEA
    # fichero = open('fichero.txt', 'r')
    # l = fichero.readline()
    # l1 = fichero.readline()
    # l2 = fichero.readline()
    # print(l)
    # print(l1)
    # print(l2)
    # fichero.close()

    # LECTURA DE LINEAS
    # with open('fichero.txt', 'r') as fichero:
    #     for linea in fichero:
    #         print(linea)
    # fichero.close()

    # PUNTERO APUNTANOD A LA POSICION 10
    # fichero = open('fichero.txt', 'r')
    # fichero.seek(10)
    # texto = fichero.read()
    # fichero.close()
    # print(texto)

    # PUNTERO APUNTANOD A LA POSICION 0
    # fichero = open('fichero.txt', 'r')
    # fichero.seek(0)
    # t = fichero.read(5)
    # fichero.seek(0)
    # texto = fichero.read()
    # fichero.seek(len(texto)/2) #  puntero en la mitad del texto
    # print(fichero.read())

    # EJERCICIO - MODO LECTURA Y ESCRITURA
    fichero = open('../fichero.txt', 'r+')
    lineas = fichero.readlines()
    lineas[2] = "Esta linea modificada"
    fichero.seek(0)
    fichero.writelines(lineas)
    fichero.close()
    print(lineas)


if __name__ == '__main__':
    main()
