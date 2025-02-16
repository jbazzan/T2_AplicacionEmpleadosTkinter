import sqlite3

conexion = sqlite3.connect('datos.db')
conexion.close

cursor=conexion.cursor()

cursor.execute("SELECT * FROM EMPLEADOS")

empleados = cursor.fetchall()

for empleado in empleados:
    print(empleado)


conexion.commit()
conexion.close()