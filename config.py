import json, os
from dotenv import load_dotenv
load_dotenv()

def get_agent_for_today(fecha):
    with open('turnos.json', 'r') as f:
        turnos = json.load(f)
    return turnos.get(fecha, {"nombre": "Sin asignar", "telefono": os.getenv("FALLBACK_PHONE")})