# Tarea Semana 13 - Creación de una Aplicación GUI Básica

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Datos U.E.A.")  # Título de la ventana

# Etiquetas y campos de texto para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)  # Ubica la etiqueta en la ventana con márgenes
entry_nombre = tk.Entry(ventana)  # Campo de entrada para el nombre
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Etiquetas y campos de texto para la cédula
label_cedula = tk.Label(ventana, text="Cédula:")
label_cedula.grid(row=1, column=0, padx=5, pady=5)
entry_cedula = tk.Entry(ventana)  # Campo de entrada para la cédula
entry_cedula.grid(row=1, column=1, padx=5, pady=5)

# Etiquetas y campos de texto para el semestre
label_semestre = tk.Label(ventana, text="Semestre:")
label_semestre.grid(row=2, column=0, padx=5, pady=5)
entry_semestre = tk.Entry(ventana)  # Campo de entrada para el semestre
entry_semestre.grid(row=2, column=1, padx=5, pady=5)

# Etiquetas y campos de texto para la especialidad
label_especialidad = tk.Label(ventana, text="Especialidad:")
label_especialidad.grid(row=3, column=0, padx=5, pady=5)
entry_especialidad = tk.Entry(ventana)  # Campo de entrada para la especialidad
entry_especialidad.grid(row=3, column=1, padx=5, pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana)
lista_datos.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Función para agregar los datos ingresados en los campos a la lista
def agregar_datos():
    # Obtiene los valores de los campos de texto
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    semestre = entry_semestre.get()
    especialidad = entry_especialidad.get()

    # Verifica que todos los campos tengan datos antes de agregarlos a la lista
    if nombre and cedula and semestre and especialidad:
        # Agrega los datos a la lista en el formato especificado
        lista_datos.insert(tk.END, f"{nombre} - {cedula} - {semestre} - {especialidad}")
        # Limpia los campos de texto después de agregar los datos
        entry_nombre.delete(0, tk.END)
        entry_cedula.delete(0, tk.END)
        entry_semestre.delete(0, tk.END)
        entry_especialidad.delete(0, tk.END)
    else:
        # Muestra una advertencia si no se han completado todos los campos
        tk.messagebox.showwarning("Advertencia", "Debe completar todos los espacios.")

# Función para limpiar todos los datos de la lista
def limpiar_datos():
    lista_datos.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Botón para agregar los datos ingresados
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.grid(row=4, column=0, padx=5, pady=5)

# Botón para limpiar la lista de datos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.grid(row=4, column=1, padx=5, pady=5)

# Ejecutar la ventana principal
ventana.mainloop()  # Mantiene la ventana abierta y funcional
