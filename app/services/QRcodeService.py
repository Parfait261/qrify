
from app.model.qr_code import qr_code
from app.schemas.qr_code import qr_code_request, qr_code_response
from app.services.QRcodeGenerator import QRcodeGenerator


class QRcodeService :
    def __init__(self, qr_code_generator : QRcodeGenerator) :
        self.qr_code_generator = qr_code_generator

    def create_qr_code(self, entry : qr_code_request) -> qr_code :
        image = self.qr_code_generator.generate_qrcode(str(entry.link))
        return qr_code(
            name= entry.nom,
            link = entry.link,
             image = image
        )
