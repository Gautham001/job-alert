import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_RECIPIENT = os.environ.get("EMAIL_RECIPIENT", EMAIL_ADDRESS)

def send_job_alert_email(new_jobs, company):
    subject = f"🆕 {len(new_jobs)} New Jobs at {company}"
    body = "Here are the latest job openings:\n\n"

    for job in new_jobs:
        body += f"{job['title']} - {job['location']}\n{job['url']}\n\n"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_RECIPIENT
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_RECIPIENT, msg.as_string())
        print(f"📧 Email sent to {EMAIL_RECIPIENT}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
