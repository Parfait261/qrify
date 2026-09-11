from fastapi import APIRouter

from app.schemas.qr_code import qr_code_request, qr_code_response
from app.services.QRcodeService import QRcodeService
from app.services.QRcodeGenerator import QRcodeGenerator

router = APIRouter(prefix="/api/v1/qrcode", tags=["qr code"] )


qr_code_generator = QRcodeGenerator()
qr_code_service = QRcodeService(qr_code_generator)

@router.post("",  response_model=qr_code_response)
def create_qr_code(request : qr_code_request) -> qr_code_response:
     qr_code = qr_code_service.create_qr_code (request)
     return qr_code