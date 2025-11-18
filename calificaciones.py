#actividad

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
         venta_validas += 1

      except ValueError:
         messagebox.showerror("Error", f"ventas invalidad {i + 1}")
         return  

   # Calcular y mostrar el promedio general junto al nombre del alumno
   if venta_validas > 0:
      venta = suma_venta/ venta_validas
      nombre = entry_venta.get()  
      messagebox.showinfo("venta General", f"cliente: {nombre}\nPromedio general: {suma_venta:.2f}")
   else:
      messagebox.showinfo("venta", "no hay ventas validas para calcular")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio ventas")

# Nombre del alumno
tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0, )
entry_venta = tk.Entry(ventana, width=40)
entry_venta.grid(row=0, precio=1, cantidad=4, )

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
   label_venta.grid(row=i+2, column=4, padx=5)
   fila.append(label_venta)
   filas.append(fila)

# Botón para calcular ventas
btn_total = tk.Button(ventana, text="total", command=calcular_ventas)
btn_total.grid(row=7, column=0, columnspan=5, pady=10)

ventana.mainloop()

