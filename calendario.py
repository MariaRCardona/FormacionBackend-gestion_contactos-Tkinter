from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']


def obtener_servicio_calendario():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service


def crear_evento_calendario(servicio, contacto, recordatorio):
    import datetime

    # Adaptar la fecha y hora del recordatorio (esto es un ejemplo,
    # necesitarás ajustar cómo obtienes la fecha/hora del recordatorio)
    now = datetime.datetime.now(datetime.timezone.utc)
    start_time = (now + datetime.timedelta(minutes=10)).isoformat() + 'Z'  # Ejemplo: 10 minutos desde ahora
    end_time = (now + datetime.timedelta(minutes=20)).isoformat() + 'Z'  # Ejemplo: 20 minutos desde ahora

    event = {
        'summary': f'Recordatorio: {contacto.nombre}',
        'description': recordatorio,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/Madrid',  # Ajusta tu zona horaria
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/Madrid',  # Ajusta tu zona horaria
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 5},  # Notificación 5 minutos antes
            ],
        },
    }

    try:
        created_event = servicio.events().insert(calendarId='primary', body=event).execute()
        print(f'Evento creado en Google Calendar: {created_event.get("htmlLink")}')
    except Exception as e:
        print(f'Ocurrió un error al crear el evento: {e}')
