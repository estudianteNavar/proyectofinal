
import tkinter as tk
from tkinter import Toplevel

#ventana principal 
ventana = tk.Tk()
ventana.title("ventana principal")
ventana.geometry("300x350")


#funcion para abrir ventana registros
def ventana_registro():
    ventana_registro = Toplevel(ventana)
    etiquetaproductos = tk.Label(ventana_registro, text= "Productos: ")
    etiquetaproductos.pack()
   

    etiquetacantidad = tk.Label(ventana_registro, text= "cantidad: ")
    etiquetacantidad.pack()
   

    etiquetaprecio = tk.Label(ventana_registro, text= "precio: ")
    precio =tk.Entry(ventana_registro)
    precio.pack()
boton = tk.Button(text="mostrar", command = ventana_registro)
boton.pack()

ventana.mainloop()