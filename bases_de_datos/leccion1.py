import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARHCAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios VALUES ('Hector', '27', 'hector@ejemplo.com')")

# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()  # Recupera el primer registro
# print(usuario)  # Lo imprime en forma de tupla

# usuarios = [
#     ('Mario', '51', 'mario@ejemplo.com'),
#     ('Mercedes', '38', 'mercedes@ejemplo.com'),
#     ('Juan', '19', 'juan@ejemplo.com')
# ]
#  Forma masiva para insertar datos a la BD
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

#  Para recuperar varios registro (de forma masica)
cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for u in usuarios:
    print(u)

conexion.commit()  # para confirmar todos los cambios realizados
conexion.close()
