# dashboard-Monitor

Sistema de monitoreo automatizado para dashboards operativos. 
Detecta códigos de error, gestiona responsables por turnos y permite ejecución manual de verificaciones desde una interfaz web.

---

##Objetivo

Reducir el tiempo de detección y reacción ante incidentes en dashboards críticos mediante automatización y notificación estructurada.

---

##¿Cómo funciona?

1. Se establece conexión (opcional) a entorno restringido vía VPN.
2. Se accede al dashboard utilizando Selenium (modo headless).
3. Se valida la presencia de códigos de error.
4. Se identifica el responsable según configuración de turnos (`turnos.json`).
5. Se dispara el flujo de notificación (estructura lista para integración real).
6. Se registra el evento para trazabilidad.

---

## Arquitectura
VPN → Selenium Check → Detección de Error
↓
Turnos (JSON)
↓
Notificación
↓
Logs

---

## Tecnologías utilizadas

- Python
- Flask
- Selenium
- JSON (configuración de turnos)
- python-dotenv (configuración por variables de entorno)

---

## Estructura del proyecto

- `app.py` → Interfaz web (Flask)
- `main.py` → Punto de entrada del monitoreo
- `dashboard_monitor.py` → Lógica de detección
- `vpn_connect.py` → Conexión a VPN
- `notifier.py` → Sistema de notificaciones
- `turnos.json` → Configuración de responsables
- `requirements.txt` → Dependencias

---

## Instalación

```bash
pip install -r requirements.txt
```
 Ejecución

Monitor:

python main.py

Interfaz web:

python app.py

Acceder en navegador:

http://127.0.0.1:5000

Configuracion de turnos
[
  {
    "fecha": "2026-01-21",
    "agente": "Nombre Apellido",
    "telefono": "+000000000"
  }
]
Posibles mejoras

Dockerización del entorno

Integración real con Twilio / Slack / Email

Logging estructurado y persistente

Tests automatizados

CI/CD con GitHub Actions

 Autor
 
NicLey
Ingeniero en Informática | Automatización | Sistemas
