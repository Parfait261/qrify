from pydantic import BaseModel, HttpUrl, EmailStr


class qr_code_request(BaseModel):
    nom : str
    link : str

class qr_code_response(BaseModel):
    name : str
    image : str
