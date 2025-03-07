from model.databases import RegisterUser, engine
from model.databases import TransactionModel
from sqlmodel import Session
import bcrypt



class User:
    def register_user(self, name, cpf, email, password):

        def set_password(password):
            #criptografa a senha
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return hashed_password.decode('utf-8')
        
        with Session(engine) as session:
            user = RegisterUser(name=name, cpf=cpf, email=email, password=set_password(password))
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
                return False
            

        
    
            #verificando senha
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print('login bem-sucedido')
                return True

            else:
                print('senha inválida')
                return False
                
          

     

            



        

        
        

