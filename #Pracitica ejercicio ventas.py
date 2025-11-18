#Pracitica ejercicio ventas

import tkinter as tk
from tkinter import messagebox

def calcular_ventas():
   suma_venta= 0
   
   for i in range(len(filas)):
      try:
         costo = float(filas[i][1].get())
         precio= float(filas[i][2].get())
         cantidad = float(filas[i][3].get())
         venta = (precio + cantidad) / 3
         filas[i][4].config(text=f"{venta:.2f}")
         
         suma_venta += venta
        

      except ValueError:
         messagebox.showerror("Error", f"ventas invalidad {i + 1}")
         return  
      
ventana = tk.Tk()
ventana.title("Ejercicio ventas")

tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0, )
entry_venta = tk.Entry(ventana, width=40)
entry_venta.grid(row=0, precio=2, cantidad=3, )


# Encabezados de tabla
encabezados = ["costo", "precio", "cantidad", "venta",]
for col, encabezado in enumerate(encabezados):
   tk.Label(ventana, text=encabezado, font=('Arial', 10, 'bold')).grid(row=1, column=col, padx=5, pady=5)

filas = []
for i in range(3):
   fila = []
   # ventas
   entry_venta = tk.Entry(ventana)
   entry_venta.grid(row=i+2, column=0, padx=5, pady=5)
   fila.append(entry_venta)
   # total
   for j in range(1, 4):
      entry_venta = tk.Entry(ventana, width=10)
      entry_venta.grid(row=i+2, column=j, padx=5)
      fila.append(entry_venta)
   # Promedio 
   label_venta = tk.Label(ventana, text="0.00", width=10, bg="lightgray")
   label_venta.grid(row=i+2,  cantidad=3, padx=5)
   fila.append(label_venta)
   filas.append(fila)

# Botón para calcular promedios
btn_total = tk.Button(ventana, text="Calcular", command=calcular_ventas)
btn_total.grid(row=7, precio=2, cantidad=3,  pady=10)

ventana.mainloop()
