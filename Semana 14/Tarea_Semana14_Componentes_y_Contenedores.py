# Tarea Semana 14 - Creación de una Aplicación de Agenda Personal

import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas
from tkinter import ttk, messagebox  # Importa ttk para widgets avanzados y messagebox para mostrar mensajes emergentes

# Crear la ventana principal
ventana = tk.Tk()  # Inicializa la ventana principal de la aplicación
ventana.title("Mi Agenda Personal")  # Establece el título de la ventana

# Lista para manejar los eventos como diccionarios
eventos = []  # Lista vacía que almacenará los eventos como diccionarios con fecha, hora y descripción

# Frame para la lista de eventos
frame_lista = ttk.Frame(ventana)  # Crea un contenedor (frame) para organizar la lista de eventos
frame_lista.pack(side="top", fill="both", expand=True)  # Empaqueta el frame en la parte superior y permite que se expanda

# Treeview para mostrar los eventos
columnas = ("fecha", "hora", "descripcion")  # Define las columnas para el Treeview
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")  # Crea un widget Treeview con encabezados
tree.heading("fecha", text="Fecha")  # Encabezado para la columna de fecha
tree.heading("hora", text="Hora")  # Encabezado para la columna de hora
tree.heading("descripcion", text="Descripción")  # Encabezado para la columna de descripción
tree.pack(side="left", fill="both", expand=True)  # Empaqueta el Treeview en el frame y permite que se expanda

# Scrollbar para la lista de eventos
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)  # Crea un scrollbar vertical para el Treeview
scrollbar.pack(side="right", fill="y")  # Empaqueta el scrollbar a la derecha del Treeview
tree.configure(yscrollcommand=scrollbar.set)  # Conecta el scrollbar con el Treeview para desplazarse

# Frame para los campos de entrada y botones
frame_entradas = ttk.Frame(ventana)  # Crea un frame para organizar los campos de entrada y botones
frame_entradas.pack(side="bottom")  # Empaqueta el frame en la parte inferior de la ventana

# Campos de entrada para la fecha, hora y descripción
etiqueta_fecha = ttk.Label(frame_entradas, text="Fecha:")  # Etiqueta para el campo de fecha
etiqueta_fecha.grid(row=0, column=0)  # Coloca la etiqueta en la fila 0, columna 0
entrada_fecha = ttk.Entry(frame_entradas)  # Campo de texto para ingresar la fecha
entrada_fecha.grid(row=0, column=1)  # Coloca el campo de texto en la fila 0, columna 1

etiqueta_hora = ttk.Label(frame_entradas, text="Hora:")  # Etiqueta para el campo de hora
etiqueta_hora.grid(row=1, column=0)  # Coloca la etiqueta en la fila 1, columna 0
entrada_hora = ttk.Entry(frame_entradas)  # Campo de texto para ingresar la hora
entrada_hora.grid(row=1, column=1)  # Coloca el campo de texto en la fila 1, columna 1

etiqueta_descripcion = ttk.Label(frame_entradas, text="Descripción:")  # Etiqueta para el campo de descripción
etiqueta_descripcion.grid(row=2, column=0)  # Coloca la etiqueta en la fila 2, columna 0
entrada_descripcion = ttk.Entry(frame_entradas)  # Campo de texto para ingresar la descripción del evento
entrada_descripcion.grid(row=2, column=1)  # Coloca el campo de texto en la fila 2, columna 1

# Botones para agregar, eliminar eventos y salir de la aplicación
boton_agregar = ttk.Button(frame_entradas, text="Agregar Evento")  # Botón para agregar un evento
boton_agregar.grid(row=3, column=0)  # Coloca el botón en la fila 3, columna 0

boton_eliminar = ttk.Button(frame_entradas, text="Eliminar Evento")  # Botón para eliminar un evento
boton_eliminar.grid(row=3, column=1)  # Coloca el botón en la fila 3, columna 1

boton_salir = ttk.Button(frame_entradas, text="Salir", command=ventana.quit)  # Botón para salir de la aplicación
boton_salir.grid(row=3, column=2)  # Coloca el botón en la fila 3, columna 2

# Función para agregar un evento a la lista
def agregar_evento():
    # Obtiene los valores de los campos de entrada
    fecha = entrada_fecha.get()  # Toma el valor del campo de fecha
    hora = entrada_hora.get()  # Toma el valor del campo de hora
    descripcion = entrada_descripcion.get()  # Toma el valor del campo de descripción

    # Agrega un nuevo evento como diccionario a la lista y lo inserta en el Treeview
    evento = {"fecha": fecha, "hora": hora, "descripcion": descripcion}  # Crea un diccionario con los datos del evento
    eventos.append(evento)  # Agrega el diccionario a la lista de eventos
    tree.insert("", "end", values=(fecha, hora, descripcion))  # Inserta el evento en el Treeview

    # Limpia los campos de entrada después de agregar el evento
    entrada_fecha.delete(0, tk.END)  # Borra el texto del campo de fecha
    entrada_hora.delete(0, tk.END)  # Borra el texto del campo de hora
    entrada_descripcion.delete(0, tk.END)  # Borra el texto del campo de descripción

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()  # Obtiene el evento seleccionado en el Treeview
    if seleccionado:  # Verifica si hay algún evento seleccionado
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?"):  # Muestra un cuadro de confirmación
            # Elimina el evento tanto de la lista como del Treeview
            for i, evento in enumerate(eventos):
                if (evento["fecha"], evento["hora"], evento["descripcion"]) == tree.item(seleccionado, "values"):
                    del eventos[i]  # Elimina el evento de la lista
                    break
            tree.delete(seleccionado)  # Elimina el evento del Treeview
    else:
        messagebox.showwarning("Advertencia", "No hay ningún evento seleccionado")  # Muestra una advertencia si no se seleccionó un evento

# Asociar las funciones a los botones
boton_agregar.config(command=agregar_evento)  # Asocia la función agregar_evento al botón "Agregar Evento"
boton_eliminar.config(command=eliminar_evento)  # Asocia la función eliminar_evento al botón "Eliminar Evento"

# Iniciar la aplicación
ventana.mainloop()  # Inicia el loop principal de la aplicación, manteniéndola activa

