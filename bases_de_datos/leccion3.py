import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute("SELECT * FROM usuarios WHERE id=1 or id=2")
# cursor.execute("UPDATE usuarios SET nombre='Freddy Portales' WHERE nombre='Freddy'")
cursor.execute("DELETE FROM usuarios WHERE dni='11111111A'")
# usuarios = cursor.fetchall()
#
# for u in usuarios:
#     print(u)

conexion.commit()
conexion.close()