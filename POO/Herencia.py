class Producto:

    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t\t{}
NOMBRE\t\t\t{}
PVP\t\t\t\t{}
DESCRIPCION\t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)


class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t\t{}
NOMBRE\t\t\t{}
PVP\t\t\t\t{}
DESCRIPCION\t\t{}
PRODUCTOR\t\t{}
DISTRIBUIDOR\t{}""".format(
            self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


if __name__ == '__main__':
    a = Adorno(2034, "Vaso Adornoado", 15, "Vaso de porcelana")
    print(a)
    print("\n######\n")
    al = Alimento(2035, "Botella de Aceite de Oliva Extra", 5, "250 ML")
    al.productor = "La Aceitera"
    al.distribuidor = "Distribuidora S.A.C"
    print(al)
