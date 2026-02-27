from dotenv import load_dotenv
import os

load_dotenv()

print("DASHBOARD_USER:", os.getenv("DASHBOARD_USER"))
print("TWILIO_SID:", os.getenv("TWILIO_SID"))
print("FALLBACK_PHONE:", os.getenv("FALLBACK_PHONE"))
