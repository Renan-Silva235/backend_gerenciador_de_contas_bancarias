from model.databases import RegisterUser, TransactionModel, RegisterUser, engine
from sqlmodel import Session, select
from entities.user import User


class Transaction:
    def deposit(self,user: RegisterUser, value: float):
        with Session(engine) as session:
            transaction = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if transaction:
                transaction.balance += value
                session.add(transaction)
                session.commit()

    
    def get_balance(self, user: RegisterUser):
        with Session(engine) as session:
            balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if balance:
                return f'saldo: R${balance.balance:.2f}'
                
            else:
                return 'CPF INVÁLIDO'
            

    def withdraw_money(self, user:RegisterUser, value: float):
         with Session(engine) as session:
            withdraw = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if withdraw:
                withdraw.balance -= value
                session.add(withdraw)
                session.commit()
               
  
            
            

       
        
