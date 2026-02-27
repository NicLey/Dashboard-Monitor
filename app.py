from flask import Flask, render_template, redirect, url_for
from dashboard_monitor import check_dashboard_error
from notifier import notify_agent
from config import get_agent_for_today
import datetime
from threading import Thread
import time

app = Flask(__name__)

latest_error = 0
last_check = None

def background_monitor():
    """Hilo que ejecuta la revisión cada 5 minutos."""
    global latest_error, last_check
    while True:
        error_code = check_dashboard_error()
        last_check = datetime.datetime.now()
        latest_error = error_code
        if error_code > 0:
            today = datetime.date.today().isoformat()
            agente = get_agent_for_today(today)
            notify_agent(agente["telefono"], error_code)
        time.sleep(300)

@app.route("/")
def index():
    today = datetime.date.today().isoformat()
    agente = get_agent_for_today(today)
    return render_template(
        "index.html",
        latest_error=latest_error,
        last_check=last_check,
        agente=agente,
    )

@app.route("/check")
def manual_check():
    global latest_error, last_check
    try:
        error_code = check_dashboard_error()
        last_check = datetime.datetime.now()
        latest_error = error_code
        if error_code > 0:
            today = datetime.date.today().isoformat()
            agente = get_agent_for_today(today)
            notify_agent(agente["telefono"], error_code)
    except Exception as e:
        print("[ERROR EN /check]", e)
    return redirect(url_for("index"))

if __name__ == "__main__":
    t = Thread(target=background_monitor, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=8000, debug=False)