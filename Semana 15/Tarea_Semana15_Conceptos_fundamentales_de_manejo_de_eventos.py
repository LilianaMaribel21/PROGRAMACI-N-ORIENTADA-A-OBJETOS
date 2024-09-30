# Tarea Semana 15 - Aplicación GUI de Lista de Tareas

import tkinter as tk
from tkinter import messagebox

# Clase principal para gestionar la aplicación de tareas
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas de Programación Orientada a Objetos - UEA")  # Título de la ventana principal

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=45)  # Establecer el ancho del campo de entrada
        self.task_entry.pack(pady=10)  # Añadir margen vertical entre el campo de entrada y otros elementos

        # Botón para añadir una nueva tarea
        self.add_task_button = tk.Button(root, text="Nueva Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)  # Añadir margen vertical

        # Botón para marcar una tarea como completada
        self.complete_task_button = tk.Button(root, text="Tarea Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)  # Añadir margen vertical

        # Botón para eliminar una tarea seleccionada
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)  # Añadir margen vertical

        # Lista para mostrar las tareas ingresadas
        self.task_listbox = tk.Listbox(root, width=50, height=10)  # Definir tamaño de la lista
        self.task_listbox.pack(pady=10)  # Añadir margen vertical entre la lista y otros elementos

        # Vincular la tecla Enter al campo de entrada para añadir tareas automáticamente
        self.task_entry.bind('<Return>', lambda event: self.add_task())

    # Método para añadir una nueva tarea
    def add_task(self):
        task = self.task_entry.get()  # Obtener el texto ingresado en el campo de entrada
        if task:  # Comprobar si el campo no está vacío
            self.task_listbox.insert(tk.END, task)  # Añadir la tarea al final de la lista
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir la tarea
        else:
            messagebox.showwarning("Advertencia", "Ingrese una tarea para comenzar.")  # Mostrar advertencia si no se ha ingresado ninguna tarea

    # Método para marcar una tarea como completada
    def complete_task(self):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)  # Obtener el texto de la tarea seleccionada
            completed_task = f"{task} (Tarea Completada)"  # Añadir la etiqueta "Tarea Completada" a la tarea
            self.task_listbox.delete(selected_index)  # Eliminar la tarea original de la lista
            self.task_listbox.insert(selected_index, completed_task)  # Insertar la tarea marcada como completada en la misma posición
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea antes de marcarla como completada.")  # Mostrar advertencia si no se ha seleccionado ninguna tarea

    # Método para eliminar una tarea seleccionada
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            self.task_listbox.delete(selected_index)  # Eliminar la tarea de la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Primero seleccione una tarea para eliminarla.")  # Mostrar advertencia si no se ha seleccionado ninguna tarea

# Configuración de la ventana principal y ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    app = TaskManagerApp(root)  # Instanciar la clase de la aplicación
    root.mainloop()  # Ejecutar el bucle principal de la interfaz gráfica
