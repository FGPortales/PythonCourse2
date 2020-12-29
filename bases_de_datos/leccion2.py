import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
# #     CREATE TABLE usuarios (
# #         dni VARCHAR(9) PRIMARY KEY,
# #         nombre VARCHAR(100),
# #         edad INTEGER,
# #         email VARCHAR(100)
# #     )
# #     ''')

# usuarios = [
#     ('11111111A', 'Freddy', '26', 'freddy@ejemplo.com'),
#     ('22222222B', 'Mario', '51', 'mario@ejemplo.com'),
#     ('33333333D', 'Mercedes', '38', 'mercedes@ejemplo.com'),
#     ('44444444E', 'Juan', '19', 'juan@ejemplo.com')
# ]
#
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
#     ''')

# productos = [
#     ('Teclado', 'Logitech', 19.95),
#     ('Pantalla 19', 'LG', 89.95),
# ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

# cursor.execute("SELECT * FROM productos")
#
# productos = cursor.fetchall()
# for p in productos:
#     print(p)

# cursor.execute('''
#     CREATE TABLE usuarios (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
#     ''')

# usuarios = [
#     ('11111111A', 'Freddy', '26', 'freddy@ejemplo.com'),
#     ('22222222B', 'Mario', '51', 'mario@ejemplo.com'),
#     ('33333333D', 'Mercedes', '38', 'mercedes@ejemplo.com'),
#     ('44444444E', 'Juan', '19', 'juan@ejemplo.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

cursor.execute("INSERT INTO usuarios VALUES (null,'33333333D', 'Mercedes', '38', 'mercedes@ejemplo.com')")

conexion.commit()
conexion.close()
