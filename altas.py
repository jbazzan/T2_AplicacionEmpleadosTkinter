from tkinter import *
from tkinter import ttk
import sqlite3

#CREACION DE LA BASE DE DATOS

def crear_base_datos():

    conexion = sqlite3.connect('datos.db')
    cursor=conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS EMPLEADOS (nomape varchar(50), fechaini varchar(10), fechanac varchar(10), direccion varchar(50), nif varchar(10), datban varchar(25), numss varchar(25), gen varchar(10), dpto varchar(20), puesto varchar(20), tel varchar(10), salanual varchar(10), irpf varchar(10), email varchar(50), pextra varchar(10), segsoc varchar(10))")

    conexion.commit()
    conexion.close()

crear_base_datos()

#REGISTRO DE EMPLEADOS

def insertar():
    conexion = sqlite3.connect('datos.db')
    cursor=conexion.cursor()

    datos = (
        nomape.get(), fechaini.get(), fechanac.get(), direccion.get(),
        nif.get(), datban.get(), numss.get(), gen.get(), dpto.get(),
        puesto.get(), tel.get(), salanual.get(), irpf.get(), email.get(),
        pextra.get(), segsoc.get()
    )

    cursor.execute("INSERT INTO EMPLEADOS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datos)

    conexion.commit()
    conexion.close()

    nomape.set("")
    fechaini.set("")
    fechanac.set("")
    direccion.set("")
    nif.set("")
    datban.set("")
    numss.set("")
    gen.set("")
    dpto.set("")
    puesto.set("")
    tel.set("")
    salanual.set("")
    irpf.set("")
    email.set("")
    pextra.set("")
    segsoc.set("")

    mensaje.set("Empleado agregado con exito!")

#Variables a utilizar

nomape=StringVar()
fechaini=StringVar()
fechanac=StringVar()
direccion=StringVar()
nif=StringVar()
datban=StringVar()
numss=StringVar()
gen=StringVar()
dpto=StringVar()
puesto=StringVar()
tel=StringVar()
salanual=StringVar()
irpf=StringVar()
email=StringVar()
pextra=StringVar()
segsoc=StringVar()
mensaje = StringVar()


def altas():

    altas=Toplevel()
    altas.title("ALTAS")
    altas.resizable(1,1)
    altas.config(bd=20)
    altas.geometry("825x375+400+200")

    #APELLIDO Y NOMBRE
    Label(altas, text="APELLIDO Y NOMBRE").grid(row=0,column=0,columnspan=6)
    Entry(altas, textvariable=nomape).grid(row=1,column=0,columnspan=6, padx=10,sticky=EW)

    #FECHA INICIO, FECHA NACIMIENTO, DIRECCION
    Label(altas, text="FECHA INICIO").grid(row=2,column=0, padx=10, pady=5)
    Entry(altas, textvariable=fechaini).grid(row=3,column=0, padx=10)

    Label(altas, text="FECHA NACIMIENTO").grid(row=2,column=1, padx=10, pady=5)
    Entry(altas, textvariable=fechanac).grid(row=3,column=1, padx=10)

    Label(altas, text="DIRECCION").grid(row=2,column=2, columnspan=4, padx=10, pady=5)
    Entry(altas, textvariable=direccion).grid(row=3,column=2,columnspan=4, padx=10, sticky=EW)

    #NIF, DATOS BANCARIOS, NUMERO DE AFILIACION SS
    Label(altas, text="NIF").grid(row=4,column=0, padx=5, pady=5)
    Entry(altas, textvariable=nif).grid(row=5,column=0)

    Label(altas, text="DATOS BANCARIOS").grid(row=4,column=2, padx=10, pady=5)
    Entry(altas, textvariable=datban).grid(row=5,column=1, columnspan=3, sticky=EW)

    Label(altas, text="NUMERO DE AFILIACION SS").grid(row=4,column=4, columnspan=2, padx=10, pady=5)
    Entry(altas, textvariable=numss).grid(row=5,column=4, columnspan=2, padx=10, sticky=EW)

    #GENERO, DEPARTAMENTO, PUESTO
    Label(altas, text="GENERO").grid(row=6,column=0, padx=5, pady=5)
    Entry(altas, textvariable=gen).grid(row=7,column=0)

    Label(altas, text="DEPARTAMENTO").grid(row=6,column=2, padx=5, pady=5)
    Entry(altas, textvariable=dpto).grid(row=7,column=1, columnspan=3, sticky=EW)

    Label(altas, text="PUESTO").grid(row=6,column=4, columnspan=2, padx=5, pady=5)
    Entry(altas, textvariable=puesto).grid(row=7,column=4, columnspan=2, padx=10, sticky=EW)

    Label(altas, text="").grid(row=8,column=0, pady=5)

    #TELEFONO, SALARIO ANUAL, IRPF
    Label(altas, text="TELEFONO").grid(row=9,column=0, padx=5, pady=5)
    Entry(altas, textvariable=tel).grid(row=9,column=1, sticky=W)

    Label(altas, text="SALARIO ANUAL").grid(row=9,column=2, padx=5, pady=5)
    Entry(altas, textvariable=salanual).grid(row=9,column=3)

    Label(altas, text="IRPF").grid(row=9,column=4, padx=5, pady=5)
    Entry(altas, textvariable=irpf).grid(row=9,column=5)

    #EMAIL, PAGAS EXTRA, SEG. SOCIAL
    Label(altas, text="EMAIL").grid(row=10,column=0, padx=5, pady=5)
    Entry(altas, textvariable=email).grid(row=10,column=1, sticky=W)

    Label(altas, text="PAGAS EXTRA").grid(row=10,column=2, padx=5, pady=5)
    Entry(altas, textvariable=pextra).grid(row=10,column=3)

    Label(altas, text="SEG. SOCIAL").grid(row=10,column=4, padx=5, pady=5)
    Entry(altas, textvariable=segsoc).grid(row=10,column=5)

    #BOTON INSERTAR
    style = ttk.Style()
    style.configure("Estilo.TButton", font=("Arial", 12, "bold"), padding=5, foreground="black", background="lightgray")
    ancho_boton = 15

    ttk.Button(altas, text="INSERTAR", width=ancho_boton, style="Estilo.TButton", command=insertar).grid(row=12, column=5, pady=15, sticky=W)

    
    mensaje.set("Bienvenido!, Listo para agregar un empleado?")
    monitor = Label(altas, textvar=mensaje)
    monitor.grid(row=12, column=0, columnspan=4, sticky=W)

    altas.mainloop()