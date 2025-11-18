#repaso actividad 15 

import tkinter as tk 

ventana = tk.Tk() #crea una ventana nueva 
ventana.title("act.15 Samantha")
ventana.geometry("300x300")

#etiqueta texto
etiqueta = tk.Label(ventana, text="nombre y apellido")

etiqueta.pack()

#cuadrso de texto 
nombre = tk.Entry(ventana)
apellido = tk.Entry(ventana)
nombre.pack()
apellido.pack()

#funcion para mostrar nombre
def mostrarnombre()
 texto = nombre.get() + " " + apellido.get()
 etiqueta_resultado.confing(text=f"{texto}")




#etiqueta con resultado
etiqueta_resultado = tk.Label(ventana,font=("arial",12), fg="orange")
etiqueta_resultado.pack(pady=20)


#boton de comando
boton = tk.Button(ventana,text="mostrar", command=mostrarnombre)
boton.pack()


#activar la ventana
ventana.mainloop()