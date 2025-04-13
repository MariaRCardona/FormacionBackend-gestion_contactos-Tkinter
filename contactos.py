import json
import re


class Contacto:
    def __init__(self, nombre, telefono, email, grupos=None, etiquetas=None, historial_interacciones=None):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.grupos = grupos or []
        self.etiquetas = etiquetas or []
        self.historial_interacciones = historial_interacciones or []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "grupos": self.grupos,
            "etiquetas": self.etiquetas,
            "historial_interacciones": self.historial_interacciones
        }

    @staticmethod
    def from_dict(data):
        return Contacto(
            data["nombre"],
            data["telefono"],
            data["email"],
            data.get("grupos", []),
            data.get("etiquetas", []),
            data.get("historial_interacciones", [])
        )


class GestionContactos:
    def __init__(self, archivo_datos="contactos.json"):
        self.archivo_datos = archivo_datos
        self.lista_contactos = self.cargar_contactos()

    def agregar_contacto(self, contacto):
        self.lista_contactos.append(contacto)
        self.guardar_contactos()

    def eliminar_contacto(self, nombre):
        self.lista_contactos = [c for c in self.lista_contactos if c.nombre != nombre]
        self.guardar_contactos()

    def buscar_contacto(self, nombre):
        return [c for c in self.lista_contactos if nombre.lower() in c.nombre.lower()]

    def buscar_por_grupo(self, grupo):
        return [c for c in self.lista_contactos if grupo in c.grupos]

    def buscar_por_etiqueta(self, etiqueta):
        return [c for c in self.lista_contactos if etiqueta in c.etiquetas]

    def guardar_contactos(self):
        with open(self.archivo_datos, "w") as f:
            json.dump([c.to_dict() for c in self.lista_contactos], f, indent=4)

    def cargar_contactos(self):
        try:
            with open(self.archivo_datos, "r") as f:
                data = json.load(f)
                return [Contacto.from_dict(c) for c in data]
        except FileNotFoundError:
            return []
