import bcrypt
import re


def set_password(password):
    #criptografa a senha

    if not re.fullmatch(r'\d{4}', password):
        raise ValueError('senha inválida')
    
  

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')
