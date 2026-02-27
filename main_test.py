from config import get_agent_for_today
import datetime

def connect_to_vpn():
    print("[Simulación] Conexión VPN omitida")

def check_dashboard_error():
    print("[Simulación] Revisando dashboard...")
    return 5  # Número ficticio de error para probar

def notify_agent(to_number, error_code):
    print(f"[Simulación] Llamando a {to_number} por error {error_code}")

if __name__ == "__main__":
    connect_to_vpn()
    error_code = check_dashboard_error()
    if error_code > 0:
        today = datetime.date.today().isoformat()
        agente = get_agent_for_today(today)
        notify_agent(agente['telefono'], error_code)