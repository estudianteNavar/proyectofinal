#ejercicio 01
#creado por: Samantha 

import tkinter as tk

ventana = tk.Tk()
ventana.title("sumar")
ventana.geometry("350x320")

entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2.pack(pady=5)

def sumar():
    
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2
        resultado.config(text=f"resultado: {suma}")
    except ValueError:
        resultado.config(text="escriba UNICAMENTE numeros")
     

boton_sumar = tk.Button(ventana, text="sumar", command=sumar)
boton_sumar.pack(pady=5)


def restar():
    
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resta = num1 - num2
        resultado.config(text=f"resultado: {resta}")
    except ValueError:
        resultado.config(text="escriba UNICAMENTE numeros")
     

boton_restar = tk.Button(ventana, text="restar", command=restar)
boton_restar.pack(pady=5)


def multiplicar():
    
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        multiplica = num1 * num2
        resultado.config(text=f"resultado: {multiplica}")
    except ValueError:
        resultado.config(text="escriba UNICAMENTE numeros")
     

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

def Dividir():
    
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        dividir = num1 % num2
        resultado.config(text=f"resultado: {dividir}")
    except ValueError:
        resultado.config(text="escriba UNICAMENTE numeros")
     

boton_dividir = tk.Button(ventana, text="Dividir", command=Dividir)
boton_dividir.pack(pady=5)


#etiqueta para mostrra resultado
resultado = tk.Label(ventana,text="resultado: ")
resultado.pack(pady=10)



ventana.mainloop()