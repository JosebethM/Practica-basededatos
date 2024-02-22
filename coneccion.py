import sqlite3

# Conexión a la base de datos SQLite (creará la base de datos si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Realiza consultas SQL según sea necesario
cursor.execute("SELECT * FROM personas")
datos = cursor.fetchall()

# Cierra la conexión
conn.close()