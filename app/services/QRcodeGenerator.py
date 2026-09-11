import  base64
import io
import qrcode

class QRcodeGenerator :
    def generate_qrcode(self, link :str):
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image()

        buffer = io.BytesIO()
        img.save(buffer, format='PNG')

        img_bytes = buffer.getvalue()
        img_base_64 = base64.b64encode(img_bytes).decode('utf-8')

        return f"data:image/png;base64,{img_base_64}"