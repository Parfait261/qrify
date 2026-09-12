import smtplib

from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings

class EmailSender:
    def send_email(
            self,
            destinataire : EmailStr,
            subject : str,
            body : str,
            attachment : bytes,
            attachment_name : str,
    ):
        msg = EmailMessage()
        msg['From'] = settings.smtp_username
        msg['To'] = destinataire
        msg['Subject'] = subject
        msg.set_content(body)
        msg.add_attachment(
            attachment,
            maintype='image',
            subtype='png',
            filename=attachment_name)

        with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(settings.smtp_username, settings.smtp_password)
            smtp.send_message(msg)