# Tarea Semana 16 - Aplicación GUI para Gestión de Tareas con Atajos de Teclado.

# Importar la librería tkinter para la creación de la interfaz gráfica
import tkinter as tk
from tkinter import messagebox  # Para mostrar cuadros de mensaje

# Definición de la clase principal que maneja la aplicación de gestión de tareas
class TaskManagerApp:
    def __init__(self, root):
        # Inicialización de la ventana principal
        self.root = root
        self.root.title("Tareas POO - UEA")  # Título de la ventana

        # Crear el campo de entrada de texto donde el usuario ingresará nuevas tareas
        self.task_entry = tk.Entry(root, width=45)  # Establece el ancho de la entrada
        self.task_entry.pack(pady=10)  # Espaciado vertical alrededor del campo de entrada

        # Crear el botón para añadir una nueva tarea a la lista
        self.add_task_button = tk.Button(root, text="Nueva Tarea", command=self.add_task)  # Botón para agregar tarea
        self.add_task_button.pack(pady=5)  # Espaciado vertical alrededor del botón

        # Crear el botón para marcar una tarea como completada
        self.complete_task_button = tk.Button(root, text="Tarea Completada", command=self.complete_task)  # Botón de completar tarea
        self.complete_task_button.pack(pady=5)  # Espaciado vertical alrededor del botón

        # Crear el botón para eliminar una tarea de la lista
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)  # Botón de eliminar tarea
        self.delete_task_button.pack(pady=5)  # Espaciado vertical alrededor del botón

        # Crear una lista visual para mostrar las tareas añadidas
        self.task_listbox = tk.Listbox(root, width=50, height=10)  # Establece el tamaño de la lista de tareas
        self.task_listbox.pack(pady=10)  # Espaciado vertical alrededor de la lista de tareas

        # Asignar atajos de teclado para manejar las tareas con teclas específicas
        self.task_entry.bind('<Return>', lambda event: self.add_task())  # Presionar Enter añade la tarea
        self.root.bind('<End>', lambda event: self.complete_task())  # Tecla End para completar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Tecla Delete para eliminar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Tecla Escape para salir de la aplicación

    # Método para añadir una tarea a la lista
    def add_task(self):
        task = self.task_entry.get()  # Obtener el texto de la barra de entrada
        if task:  # Si la entrada no está vacía
            self.task_listbox.insert(tk.END, task)  # Insertar la tarea al final de la lista de tareas
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir la tarea
        else:
            # Mostrar una advertencia si el usuario intenta añadir una tarea vacía
            messagebox.showwarning("Advertencia", "Ingrese una tarea para comenzar.")

    # Método para marcar una tarea como completada
    def complete_task(self):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)  # Obtener el texto de la tarea seleccionada
            completed_task = f"{task} (Tarea Completada)"  # Añadir la marca de "Tarea Completada"
            self.task_listbox.delete(selected_index)  # Eliminar la tarea original
            self.task_listbox.insert(selected_index, completed_task)  # Reinsertar la tarea completada en su lugar original
        except IndexError:
            # Mostrar una advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Seleccione una tarea antes de marcarla como completada.")

    # Método para eliminar una tarea de la lista
    def delete_task(self):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)  # Eliminar la tarea seleccionada
        except IndexError:
            # Mostrar una advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("Advertencia", "Primero seleccione una tarea para eliminarla.")

# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de la aplicación
    app = TaskManagerApp(root)  # Instanciar la clase principal de la aplicación
    root.mainloop()  # Iniciar el bucle principal de eventos de la aplicación
