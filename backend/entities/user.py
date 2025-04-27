from backend.model.databases import RegisterUser, engine
from backend.model.databases import TransactionModel
from sqlmodel import Session
import bcrypt
from backend.validations.validate_password import set_password
from backend.validations.validate_email import valid_email
from backend.validations.validate_cpf import valid_cpf

class User:
    def register_user(self, name, cpf, email, password, confirm_password):
        
        with Session(engine) as session:
            email_validated = valid_email(email)
            password_validated = set_password(password, confirm_password)
            
            
            user = RegisterUser(name=name.title(), cpf=valid_cpf(cpf), email=email_validated, password=password_validated)
            session.add(user)
            session.commit()
            session.refresh(user)

            transaction = TransactionModel(user_id=user.user_id, balance=0)
            session.add(transaction)
            session.commit()

            



    def login(self, cpf, password):

        #verificar cpf
        with Session(engine) as session:

            user = session.query(RegisterUser).filter(RegisterUser.cpf == cpf).first()

            if user is None:
                print('cpf inválido')
                return None
            

            #verificando senha
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print('login bem-sucedido')
                return user

            else:
                print('senha inválida')
                return None
                
          

     

            



        

        
        

