from tkinter import *
from tkinter import ttk

def exportar_datos_a_txt():
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM EMPLEADOS")
    empleados = cursor.fetchall()

    conexion.close()

    with open("empleados.txt", "w", encoding="utf-8") as archivo:
        for empleado in empleados:
            archivo.write(f"{empleado[0]}\n")
            archivo.write(f"{empleado[3]}\n")
            archivo.write(f"NIF: {empleado[4]}")
            archivo.write(f" NAF: {empleado[6]}")
            archivo.write(f"   CCC: {empleado[5]}\n")
            archivo.write(f"CONCEPTOS SALARIALES -------------------------------------------------------------------\n")
            archivo.write(f"SALARIO ANUAL: {empleado[11]}")
            archivo.write(f"   PAGAS: {empleado[14]}")
            archivo.write(f"   IRPF: {empleado[12]}")
            archivo.write(f"   SEGURIDAD SOCIAL: {empleado[15]}\n\n\n")

root = Tk()

from altas import *

root.config(bd=20)
root.title("Aplicación empleados Tkinter")
root.geometry("700x350+250+400") 
root.resizable(0,0)
root.iconbitmap("seta.ico")

style = ttk.Style()
style.configure("Estilo.TButton", font=("Arial", 14, "bold"), padding=10, foreground="black", background="lightgray")

ancho_boton = 20

imagen = PhotoImage(file="seta.png").subsample(2)

Label(root, text="PERSONAL +", font=("Arial", 14,"bold")).pack()
Label(root, text="").pack()

Label(root, image = imagen).pack()
Label(root, text="").pack()
ttk.Button(root, text="ALTA EMPLEADO", width=ancho_boton, style="Estilo.TButton", command=altas).pack()
Label(root, text="").pack()
ttk.Button(root, text="FICHERO EMPLEADO", width=ancho_boton, style="Estilo.TButton", command=exportar_datos_a_txt).pack()

root.mainloop()