
import requests
import smtplib
import json
from email.mime.text import MIMEText

with open("config.json") as f:
    cfg = json.load(f)

FROM_EMAIL = cfg["FROM_EMAIL"]
APP_PASSWORD = cfg["APP_PASSWORD"]
TO_EMAIL = cfg["TO_EMAIL"]

def search_jobs():
    query = "supply chain logistics jobs in big tech and startups"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    return f"Daily Job Search Results:\n\nSearch URL: {url}\n\nPlease refine by adding APIs for job portals."

def send_email(body):
    msg = MIMEText(body)
    msg['Subject'] = "Daily Supply Chain & Logistics Job Alerts"
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(FROM_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    content = search_jobs()
    send_email(content)
