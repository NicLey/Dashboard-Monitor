from twilio.rest import Client
import os, csv, datetime
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
from_number = os.getenv("TWILIO_FROM")

def notify_agent(to_number, error_code):
    print(f"[Simulación] Llamando a {to_number} por error {error_code}")
    with open("logs/errores.csv", "a", encoding="utf-8") as f:
        f.write(f"Llamada simulada - Tel: {to_number}, Código: {error_code}\n")
