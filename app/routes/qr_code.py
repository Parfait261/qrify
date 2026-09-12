from fastapi import APIRouter

from app.schemas.qr_code import qr_code_request, qr_code_response
from app.services.QRcodeService import QRcodeService
from app.services.QRcodeGenerator import QRcodeGenerator
from app.schemas.qr_code import qr_code_email_request
from app.services.EmailSender import EmailSender
from app.services.EmailService import EmailService

router = APIRouter(prefix="/api/v1/qrcode", tags=["qr code"] )


qr_code_generator = QRcodeGenerator()
qr_code_service = QRcodeService(qr_code_generator)
email_sender = EmailSender()
email_service = EmailService(email_sender)

@router.post("",  response_model=qr_code_response)
def create_qr_code(request : qr_code_request) -> qr_code_response:
     qr_code = qr_code_service.create_qr_code (request)
     return qr_code

@router.post("/email")
def send_qr_code_by_email(
    request: qr_code_email_request
):
    email_service.send_qr_code(
        email=request.email,
        nom=request.nom,
        image=request.image
    )

    return {
        "message": "QR code envoyé par email"
    }