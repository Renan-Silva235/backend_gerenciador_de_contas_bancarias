import bcrypt
import re
from backend.exceptions.excecoes import PasswordDoNotMatch

def set_password(password, confirm_password):

    if not re.fullmatch(r'\d{4}', password):
        raise ValueError('senha inválida')
    
    if password == confirm_password:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
    else:
        raise PasswordDoNotMatch('As senhas não coincidem.')

    
