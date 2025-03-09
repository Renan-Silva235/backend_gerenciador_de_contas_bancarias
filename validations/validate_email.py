from pydantic import EmailStr, BaseModel, ValidationError

class EmailValidator(BaseModel):
    email: EmailStr


def valid_email(email):
    try:
        validate_email = EmailValidator(email=email)
        return validate_email.email
    except ValidationError as error:
        return None