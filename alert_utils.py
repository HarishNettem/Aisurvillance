import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# === Email Configuration ===
EMAIL_SENDER = 'kalyansingamsetty2@gmail.com'
EMAIL_PASSWORD = 'wtor oqtw aogs cquk'  # Use Gmail App Password
EMAIL_RECEIVERS = ['22ht1a43a4@gmail.com']  # list of receivers

# === Twilio SMS Configuration ===
TWILIO_ACCOUNT_SID = 'ACe02f87010b0bc92b0e3a56cb0384cc09'
TWILIO_AUTH_TOKEN = 'f4de12a176dae159608b7bd489facf7f'
TWILIO_FROM_NUMBER = '+917981144254'  # Twilio-verified number
TO_PHONE_NUMBERS = ['+918919261121']  # Format with country code

# === Send Email Alert ===
def send_email_alert(subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_RECEIVERS)
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
        server.quit()
        print("[✔] Email alert sent.")
    except Exception as e:
        print(f"[✖] Failed to send email: {e}")

# === Send SMS Alert ===
def send_sms_alert(message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        for number in TO_PHONE_NUMBERS:
            client.messages.create(
                body=message,
                from_=TWILIO_FROM_NUMBER,
                to=number
            )
        print("[✔] SMS alert sent.")
    except Exception as e:
        print(f"[✖] Failed to send SMS: {e}")

# === Main Alert Function ===
def send_alert(message):
    send_email_alert("Smart Surveillance Alert", message)
    send_sms_alert(message)  # Optional: comment out if not using SMS
