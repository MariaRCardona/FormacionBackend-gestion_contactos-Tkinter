# 🗂️ Sistema de Gestión de Contactos con Tkinter

Este proyecto permite gestionar contactos mediante una interfaz gráfica desarrollada en Tkinter. Integra funcionalidades para añadir, eliminar contactos, y crear recordatorios que pueden ser sincronizados con Google Calendar.

![CONTACT US](https://github.com/user-attachments/assets/7dd2e1ab-c8dd-4c72-b7ca-0fe5b22f1b25)

## Objetivo del proyecto
Desarrollado como parte del proyecto personal para el programa de Formación Avanzada en Desarrollo Backend (Python, Flask, Django) – IBM SkillsBuild / Bejob, este sistema tiene como finalidad:
- Aplicar habilidades de desarrollo de interfaces gráficas con Python.
- Integrar servicios en la nube utilizando APIs externas (Google Calendar).
- Implementar buenas prácticas de almacenamiento y manejo de datos locales.
- Ofrecer una solución práctica para la automatización de la gestión de contactos y recordatorios.

##  Funcionalidades principales

-  Agregar contactos (nombre, teléfono, email)
-  Eliminar contactos seleccionados
-  Crear recordatorios desde la interfaz
-  Integración con Google Calendar (OAuth)
-  Interfaz gráfica amigable con fondo personalizado


## 🛠️ Tecnologías utilizadas

- Python 3
- Tkinter
- JSON para almacenamiento
- Google API (Calendar)
- PIL para manejo de imágenes


##  Estructura del proyecto
```
gestion_contactos/
├── calendario.py            # Lógica para recordatorios en Google Calendar
├── cargar_imagenes.py       # Función para cargar imágenes en la interfaz
├── contactos.py             # CRUD de contactos (guardar, cargar, eliminar)
├── contactos.json           # Archivo de almacenamiento local de contactos
├── credentials.json         # Credenciales OAuth de Google
├── ejecutar.py              # Script principal para lanzar la aplicación
├── fondo.jpg                # Imagen de fondo de la interfaz
├── gui.py                   # Interfaz gráfica Tkinter
├── preview_tkinter.png      # Captura de pantalla de la app en ejecución
├── quickstart.py            # Configuración inicial de Google Calendar API
├── token.json               # Token OAuth para acceder a la cuenta de Google
└── token.pickle             # Archivo de sesión OAuth
```

## Demostración de la aplicación

Puedes ver el funcionamiento de la aplicación en este video: [Demostración en YouTube]([https://www.youtube.com/watch?v=TU_ID_DEL_VIDEO](https://youtu.be/y9etWK2sf7o))

##
**María José Rivas Cardona**
Este sistema fue desarrollado como parte de un proyecto personal para la Formación Avanzada en Desarrollo Backend (Python, Flask, Django) (En curso) IBM SkillsBuild / Bejob para automatizar la gestión de contactos con recordatorios integrados usando Python, Tkinter y Google Calendar.

