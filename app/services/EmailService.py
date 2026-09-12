import base64

from  app.services.EmailSender import EmailSender

class EmailService:
    def __init__(self, email_sender: EmailSender):
        self.email_sender = EmailSender()

    def send_qr_code(self, email : str, nom :str, image : str):
        img_base64 = image.split(",", 1)[1]
        img_bytes =  base64.b64decode(img_base64)

        self.email_sender.send_email(
            destinataire=email,
            subject=f"Votre QR Code - {nom}",
            body=f"Bonjour,\n\nVoici votre QR Code pour : {nom}.",
            attachment=img_bytes,
            attachment_name=f"{nom}.png"
        )