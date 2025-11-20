
#proyectofinal
#submodulo
#Autores: Navar Galindo y Ocaña Vela 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesita instalar pillow: pip install pillow
import os 


def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


ventana = tk.Tk()
ventana.title("punto de ventas- videojuego ")
ventana.geometry("500x600")
ventana.configure(bg="#44505c") # Color de fondo claro


try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR,"ventas2025.png")) 
    imagen = imagen.resize((250, 250)) 
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
   lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
   lbl_sin_logo.pack(pady=40)


# BOTONES PRINCIPALES
# -------------------------
estilo = ttk.Style()
estilo.configure(
    "TButton",
    font=("Arial", 12),
    padding=10,
    background="#2d89ef"
)
estilo.map(
    "TButton",
    background=[("active", "#1e5fab")]  # Color al presionar
)

btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", width=25, command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", width=25, command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", width=25, command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", width=25, command=abrir_acerca_de)
btn_acerca.pack(pady=10)


ventana.mainloop()