from pydantic import EmailStr, BaseModel, ValidationError
from backend.exceptions.excecoes import EmailInvalid

class EmailValidator(BaseModel):
    email: EmailStr


def valid_email(email):
    try:
        validate_email = EmailValidator(email=email)
        return validate_email.email
    except ValidationError:
        raise EmailInvalid('E-mail inválido')