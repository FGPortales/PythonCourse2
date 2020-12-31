import re


texto = "En esta cadena se encuentra una palabra magica"

print(re.search('magica', texto))

palabra = 'magica'
encontrado = re.search(palabra, texto)

if encontrado is not None:
    print("Se ha encontrado la palabra")
else:
    print("No se ha encontrado la palabra")

encontrado = re.search(palabra, texto)

print(encontrado.start())
print(encontrado.end())
print(encontrado.span())
print(encontrado.string)  # para recuperar la frase en donde hemos enocntrado

texto = "Hola Mundo"
print(re.match("Hola", texto))

texto = "Vamos a dividir esta cadena"
print(re.split(' ', texto))

texto = "Hola amigo"
print(re.sub("amigo", "amiga", texto))

texto = "Hola adios hola hola"
print(re.findall("hola", texto))

texto = "Hola adios hello bye"
print(re.findall("(Hola|hello)", texto))

# ===========================

texto = "hla hola hoola hooola hoooooola"
print(re.findall('hla', texto), 'g')


def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))


print("======")
patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto)
print("======")

texto = "hla hola hoola hooola hoooooola"
patrones = ['ho', 'ho*', 'ho*la', 'hu*la']
buscar(patrones, texto)
print("======")

texto = "hla hola hoola hooola hoooooola"
patrones = ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(patrones, texto)
print("======")

texto = "hla hola hoola hooola hoooooola"
patrones = ['ho{0}la', 'ho{1}la', 'ho{3}la']
buscar(patrones, texto)
print("======")

texto = "hla hola hoola hooola hoooooola"
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,10}la']
buscar(patrones, texto)
print("======")

texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)
print("======")

texto = "haala heeela hiiiila hooooola"
patrones = ['h[ae]la', 'h[ae]*la', 'h[io]*la']
buscar(patrones, texto)
print("======")

# Exclusión
texto = "hala hela hila hola hula"
patrones = ['h[o]la', 'h[^o]la']
buscar(patrones, texto)
print("======")

# Rangos
texto = "hola h0la Hola mola m0la M0la sdjh sdZd U377"
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}']
buscar(patrones, texto)
print("======")

# Caracteres Escapados
texto = "Este curso de Python 3 se publicó en el año 2016"
patrones = [r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\S+', r'\w', r'\w+', r'\W' , r'\W+']
buscar(patrones, texto)
