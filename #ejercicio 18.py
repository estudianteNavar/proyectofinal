#ejercicio 18

import tkinter as tk
from tkinter import messagebox
from tkinter import font

#ventana principal 
ventana = tk.Tk()
ventana.title("verificacion de acceso")
ventana.geometry("300x300")
ventana.configure(bg="#f3f3f3") # color de fondo claro

# Fuente personalizada
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_normal = font.Font(family="Helvetica", size=10)

# Marco centrado
marco = tk.Frame(ventana, bg="#10bd92", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")


# Etiqueta de título
etiqueta = tk.Label(marco, text="Ingrese su contraseña", font=fuente_titulo, bg="#0fbe93")
etiqueta.pack(padx=20, pady=(15, 5))

# Campo de entrada de password
entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)



 # Función para verificar la contraseña
def verificar_password():
   password = entrada_password.get()
   if password == "admin123":
      messagebox.showinfo("Acceso", "Acceso correcto")
   else:
      messagebox.showerror("Acceso", "Acceso denegado")

   #Botón de verificación
boton_verificar = tk.Button(
marco, text="Verificar acceso", command=verificar_password,
bg="#129977", fg="white", font=fuente_normal, padx=10, pady=5,
activebackground="#45a089", relief="flat"
)
boton_verificar.pack(pady=(10, 15))


ventana.mainloop()


