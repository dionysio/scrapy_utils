import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient, message, subject=''):
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    sender_email = os.getenv('SMTP_USERNAME')
    sender_password = os.getenv('SMTP_PASSWORD')

    # Create message
    envelope = MIMEMultipart()
    envelope['From'] = sender_email
    envelope['To'] = recipient
    envelope['Subject'] = subject

    envelope.attach(MIMEText(message))

    with smtplib.SMTP(smtp_server, 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        return smtp.sendmail(sender_email, recipient, envelope.as_string())
