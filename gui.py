import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from contactos import GestionContactos, Contacto
from calendario import obtener_servicio_calendario, crear_evento_calendario
import re


class ContactosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Contactos")
        self.gestion_contactos = GestionContactos()
        self.servicio_calendario = obtener_servicio_calendario()

        # Fondo
        self.imagen_fondo = ImageTk.PhotoImage(Image.open("fondo.jpg"))
        fondo_label = tk.Label(root, image=self.imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        self._crear_widgets()
        self._mostrar_contactos()

    def _crear_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill='both', expand=True)

        # Botones
        ttk.Button(frame, text="Agregar Contacto", command=self._mostrar_dialogo_agregar).grid(row=0, column=0, padx=5)
        ttk.Button(frame, text="Eliminar Contacto", command=self._eliminar_contacto).grid(row=0, column=1, padx=5)
        ttk.Button(frame, text="Crear Recordatorio", command=self._crear_recordatorio).grid(row=0, column=2, padx=5)

        # Tabla
        self.contactos_tree = ttk.Treeview(frame, columns=("Nombre", "Teléfono", "Email"), show='headings')
        self.contactos_tree.heading("Nombre", text="Nombre")
        self.contactos_tree.heading("Teléfono", text="Teléfono")
        self.contactos_tree.heading("Email", text="Email")
        self.contactos_tree.grid(row=1, column=0, columnspan=3, pady=10, sticky='nsew')

        # Redimensionamiento
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

    def _mostrar_contactos(self):
        for i in self.contactos_tree.get_children():
            self.contactos_tree.delete(i)
        for contacto in self.gestion_contactos.lista_contactos:
            self.contactos_tree.insert("", tk.END, values=(contacto.nombre, contacto.telefono, contacto.email))

    def _mostrar_dialogo_agregar(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Agregar Contacto")

        ttk.Label(dialog, text="Nombre").grid(row=0, column=0)
        nombre_entry = ttk.Entry(dialog)
        nombre_entry.grid(row=0, column=1)

        ttk.Label(dialog, text="Teléfono").grid(row=1, column=0)
        telefono_entry = ttk.Entry(dialog)
        telefono_entry.grid(row=1, column=1)

        ttk.Label(dialog, text="Email").grid(row=2, column=0)
        email_entry = ttk.Entry(dialog)
        email_entry.grid(row=2, column=1)

        def guardar():
            nombre = nombre_entry.get()
            telefono = telefono_entry.get()
            email = email_entry.get()
            if not nombre or not telefono:
                messagebox.showerror("Error", "Nombre y teléfono obligatorios.")
                return
            if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showerror("Error", "Email inválido.")
                return
            contacto = Contacto(nombre, telefono, email)
            self.gestion_contactos.agregar_contacto(contacto)
            self._mostrar_contactos()
            dialog.destroy()

        ttk.Button(dialog, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=10)

    def _eliminar_contacto(self):
        seleccionado = self.contactos_tree.selection()
        if not seleccionado:
            messagebox.showinfo("Aviso", "Selecciona un contacto.")
            return
        index = self.contactos_tree.index(seleccionado[0])
        self.gestion_contactos.eliminar_contacto(index)
        self._mostrar_contactos()

    def _crear_recordatorio(self):
        seleccionado = self.contactos_tree.selection()
        if not seleccionado:
            messagebox.showinfo("Aviso", "Selecciona un contacto.")
            return
        index = self.contactos_tree.index(seleccionado[0])
        contacto = self.gestion_contactos.lista_contactos[index]

        dialog = tk.Toplevel(self.root)
        dialog.title("Crear Recordatorio")

        ttk.Label(dialog, text="Mensaje del recordatorio:").pack(pady=5)
        texto = tk.Text(dialog, height=5, width=40)
        texto.pack()

        def crear():
            mensaje = texto.get("1.0", tk.END).strip()
            if not mensaje:
                messagebox.showerror("Error", "Mensaje vacío.")
                return
            crear_evento_calendario(self.servicio_calendario, contacto, mensaje)
            dialog.destroy()

        ttk.Button(dialog, text="Crear", command=crear).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    app = ContactosGUI(root)
    root.mainloop()
