
from cgitb import text
from tkinter import Button, Tk
from turtle import title
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from click import command

raiz=Tk()

Label(None,text="Ingrese el idendificador").pack()

entry = ttk.Entry()
entry.pack()

def abrirArchivo():
    archivo=filedialog.askopenfilename(title='abrir')
    print(archivo)

def guardararchivo():
    guardarArch=filedialog.asksaveasfile(title='Guardar')
    print(guardarArch)

Button(raiz,text='Abrir Archivo',command=abrirArchivo).pack()
Button(raiz,text='Guardar Archivo',command=guardararchivo).pack()

raiz.mainloop()