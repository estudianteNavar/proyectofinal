#actividad 2

import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

#ejercicio 03 Navar Galindo 

#la siguiente linea obtiene los arcgivos del proyecto 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
frutas = {
    "Manzana": os.path.join(BASE_DIR, "Manzana.JPEG"),
    "Naranja": os.path.join(BASE_DIR, "Naranja.JPEG"),
    "Pera": os.path.join(BASE_DIR, "Pera.JPEG"),
    "Uvas": os.path.join(BASE_DIR, "Uvas.JPEG")
}

def mostrar_imagen(event):
    seleccion = lista_figures.get(lista_figures.curselection())
    ruta = frutas.get(seleccion)
    imagen = Image.open(ruta)
    imagen = imagen.resize((200,200))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    

ventana = tk.Tk()
ventana.title("ejercicio 03")
ventana.geometry("400x400")    


titulo = tk.Label(ventana, text="selecciona una figura", font=("arial", 14))
titulo.pack(padx=10)

lista_figures = tk.Listbox(ventana, font=("Arial", 13), height=4)
for figura in frutas.keys():
    lista_figures.insert(tk.END,figura)
    lista_figures.pack()


etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(padx=20)

def bajar_imagen():
    # Verificar que haya una imagen cargada para animar
    if not hasattr(etiqueta_imagen, 'image'):
        return  # No hacer nada si no hay imagen

def mostrar_imagen(event):
    seleccion = lista_figures.get(lista_figures.curselection())
    ruta = frutas.get(seleccion)
    imagen = Image.open(ruta)
    imagen = imagen.resize((200,200))
    imagen_tk = ImageTk.PhotoImage(imagen)

    y_inicial = 400
    y_final = 150
    velocidad = 5

    def animar(y_actual):
        if y_actual > y_final:
            etiqueta_imagen.place(x=100, y=y_actual)  # Ajusta x si quieres
            etiqueta_imagen.config(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk
            ventana.after(10, animar, y_actual - velocidad)
        else:
            etiqueta_imagen.place(x=100, y=y_final)
            etiqueta_imagen.config(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk

    animar(y_inicial)



#la siguiente linea ejecuta la funcion de
lista_figures.bind("<<ListboxSelect>>" ,mostrar_imagen)

boton_bajar = tk.Button(ventana, text="Bajar imagen", command=bajar_imagen)
boton_bajar.pack(pady=10)

ventana.mainloop()
    