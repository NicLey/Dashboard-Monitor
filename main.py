from vpn_connect import connect_to_vpn
from dashboard_monitor import check_dashboard_error
from notifier import notify_agent
from config import get_agent_for_today
import datetime

if __name__ == "__main__":
    connect_to_vpn()
    error_code = check_dashboard_error()
    if error_code > 0:
        today = datetime.date.today().isoformat()
        agente = get_agent_for_today(today)
        notify_agent(agente['telefono'], error_code)