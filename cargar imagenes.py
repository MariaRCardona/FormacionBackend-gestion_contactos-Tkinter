import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ContactosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Contactos")

        # Imagen de fondo
        self.imagen_fondo = ImageTk.PhotoImage(Image.open("fondo.jpg"))
        self.fondo_label = tk.Label(root, image=self.imagen_fondo)
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Botón agregar contacto
        self.imagen_agregar = ImageTk.PhotoImage(Image.open("agregar.jpg"))
        self.boton_agregar = tk.Button(root, image=self.imagen_agregar, command=self.agregar_contacto)
        self.boton_agregar.pack()

    def agregar_contacto(self):
        # Lógica para agregar contacto...
        def _mostrar_dialogo_agregar(self):
            dialog = tk.Toplevel(self.root)
            dialog.title("Agregar Nuevo Contacto")

            ttk.Label(dialog, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
            nombre_entry = ttk.Entry(dialog)
            nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

            ttk.Label(dialog, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
            telefono_entry = ttk.Entry(dialog)
            telefono_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

            ttk.Label(dialog, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
            email_entry = ttk.Entry(dialog)
            email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

            def agregar():
                nombre = nombre_entry.get()
                telefono = telefono_entry.get()
                email = email_entry.get()

                if not nombre or not telefono:
                    messagebox.showerror("Error", "Nombre y teléfono son obligatorios.")
                    return

                if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    messagebox.showerror("Error", "Formato de email inválido.")
                    return

                nuevo_contacto = Contacto(nombre, telefono, email)
                self.gestion_contactos.agregar_contacto(nuevo_contacto)
                self._mostrar_contactos()  # Actualizar la lista en la GUI
                dialog.destroy()

            ttk.Button(dialog, text="Guardar", command=agregar).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        def _mostrar_contactos(self):
            for item in self.contactos_tree.get_children():
                self.contactos_tree.delete(item)

            for i, contacto in enumerate(self.gestion_contactos.lista_contactos):
                self.contactos_tree.insert("", tk.END, text=i + 1, values=(
                    contacto.nombre, contacto.telefono, contacto.email, ", ".join(contacto.grupos),
                    ", ".join(contacto.etiquetas)))

        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactosGUI(root)
    root.mainloop()
