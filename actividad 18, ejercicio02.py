import tkinter as tk
from tkinter import messagebox
from tkinter import font

#--- VENTANA DE ACCESO (PRINCIPAL) ---
ventana = tk.Tk()
ventana.title("Verificación de Acceso")
ventana.geometry("300x300")
ventana.configure(bg="#f3f3f3") # Color de fondo claro

# Fuente personalizada
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_normal = font.Font(family="Helvetica", size=10)

# Marco centrado
marco = tk.Frame(ventana, bg="#10bd92", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de título
etiqueta = tk.Label(marco, text="Ingrese su contraseña", font=fuente_titulo, bg="#0fbe93", fg="white")
etiqueta.pack(padx=20, pady=(15, 5))

# Campo de entrada de password
entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)

#nueva ventana y verificacion 
def verificar_password():
    """
    Verifica la contraseña. Si es correcta, cierra la ventana actual
    y abre una nueva ventana de bienvenida.
    """
    password = entrada_password.get()
    if password == "admin123":
        # Cierra la ventana de login
        ventana.destroy()

        # Crea la nueva ventana de bienvenida
        ventana_bienvenida = tk.Tk()
        ventana_bienvenida.title("ventana principal")
        ventana_bienvenida.geometry("400x200")
        ventana_bienvenida.configure(bg="#21d4b6")

        # Mensaje de bienvenida
        etiqueta_bienvenida = tk.Label(
            ventana_bienvenida,
            text="¡Bienvenida al sistema Samantha!",
            font=fuente_titulo,
            bg="#21d4b6",
            pady=20
        )
        etiqueta_bienvenida.pack(expand=True)

        # Inicia el bucle para la nueva ventana
        ventana_bienvenida.mainloop()

    else:
        messagebox.showerror("Acceso", "Acceso denegado")

#--- BOTÓN DE VERIFICACIÓN ---
boton_verificar = tk.Button(
    marco, text="Verificar acceso", command=verificar_password,
    bg="#129977", fg="white", font=fuente_normal, padx=10, pady=5,
    activebackground="#45a089", relief="flat"
)
boton_verificar.pack(pady=(10, 15))

# Inicia el bucle de eventos para la ventana principal
ventana.mainloop()