from backend.model.databases import RegisterUser, TransactionModel, RegisterUser, engine
from sqlmodel import Session
from backend.query.query_target_user import query_target_user
from decimal import Decimal




class Transaction:
    def deposit(self,user: RegisterUser, value: str):
        with Session(engine) as session:
            transaction = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if transaction:
                transaction.balance += Decimal(value).quantize(Decimal('0.01'))
                session.add(transaction)
                session.commit()

    
    
    
    
    def get_balance(self, user: RegisterUser):
        with Session(engine) as session:
            balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if balance:
                return f'saldo: R${balance.balance}'
                
            else:
                return 'CPF INVÁLIDO'
            


    def withdraw_money(self, user:RegisterUser, value: str):
         with Session(engine) as session:
            withdraw = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if withdraw:
                withdraw.balance -= Decimal(value).quantize(Decimal('0.01'))
                session.add(withdraw)
                session.commit()


    
    def transfer(self, user:RegisterUser, cpf, value: str):

        with Session(engine) as session:
            query_balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if query_balance:
                if query_balance.balance >= Decimal(value):
                    send_money = query_target_user(cpf, value)

                    if send_money is True:
                        query_balance.balance -= Decimal(value).quantize(Decimal('0.01'))
                    
                    session.add(query_balance)
                    session.commit()
                    return 'Transferência concluída'
                else:
                    return 'Saldo insuficiente'
            
            

       
        
