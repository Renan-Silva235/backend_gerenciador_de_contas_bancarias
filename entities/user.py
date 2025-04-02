from model.databases import RegisterUser, engine
from model.databases import TransactionModel
from sqlmodel import Session
import bcrypt
from validations.validate_password import set_password
from validations.validate_email import valid_email
from validations.validate_cpf import valid_cpf


class User:
    def register_user(self, name, cpf, email, password):
        
        with Session(engine) as session:
            email_validated = valid_email(email)

            if email_validated is None:
                return 'E-mail-inválido'
            
            user = RegisterUser(name=name.title(), cpf=valid_cpf(cpf), email=email_validated, password=set_password(password))
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
                
          

     

            



        

        
        

