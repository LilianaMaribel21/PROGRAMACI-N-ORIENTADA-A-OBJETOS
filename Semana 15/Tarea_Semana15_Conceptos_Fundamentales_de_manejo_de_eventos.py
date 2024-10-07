# Tarea Semana 15 - Aplicación GUI de Lista de Tareas

import tkinter as tk
from tkinter import messagebox

# Clase principal que gestiona la aplicación del gestor de tareas
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas POO - UEA")  # Título de la ventana principal

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=45)  # Definir ancho del campo de entrada de tareas
        self.task_entry.pack(pady=10)  # Añadir espaciado vertical entre widgets

        # Botón para añadir una nueva tarea
        self.add_task_button = tk.Button(root, text="Nueva Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)  # Añadir espaciado entre el botón y otros widgets

        # Botón para marcar una tarea como completada
        self.complete_task_button = tk.Button(root, text="Tarea Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar una tarea seleccionada
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Listbox para mostrar la lista de tareas actuales
        self.task_listbox = tk.Listbox(root, width=50, height=10)  # Definir tamaño del cuadro de lista
        self.task_listbox.pack(pady=10)

        # Vincular la tecla 'Enter' con la función de añadir tarea
        self.task_entry.bind('<Return>', lambda event: self.add_task())

    # Método para añadir una nueva tarea a la lista
    def add_task(self):
        task = self.task_entry.get()  # Obtener el texto del campo de entrada
        if task:  # Comprobar si el campo no está vacío
            self.task_listbox.insert(tk.END, task)  # Añadir la tarea al final de la lista de tareas
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir la tarea
        else:
            # Mostrar advertencia si no se ha ingresado ninguna tarea
            messagebox.showwarning("Advertencia", "Ingrese una tarea para comenzar.")

    # Método para marcar una tarea seleccionada como completada
    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            task = self.task_listbox.get(selected_index)  # Obtener el texto de la tarea seleccionada
            completed_task = f"{task} (Tarea Completada)"  # Modificar el texto para indicar que está completada
            self.task_listbox.delete(selected_index)  # Eliminar la tarea original de la lista
            self.task_listbox.insert(selected_index, completed_task)  # Insertar la tarea completada en la misma posición
        except IndexError:
            # Mostrar advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Seleccione una tarea antes de marcarla como completada.")

    # Método para eliminar una tarea seleccionada de la lista
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            self.task_listbox.delete(selected_index)  # Eliminar la tarea seleccionada de la lista
        except IndexError:
            # Mostrar advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Primero seleccione una tarea para eliminarla.")

# Inicialización y ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManagerApp(root)  # Instanciar la clase de la aplicación
    root.mainloop()  # Iniciar el bucle de eventos de la interfaz gráfica
