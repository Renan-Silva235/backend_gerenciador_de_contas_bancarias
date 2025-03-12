from model.databases import RegisterUser, TransactionModel, RegisterUser, engine
from sqlmodel import Session
from query.query_target_user import query_target_user



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
print('ola')
            

    
    
    
    
    
    def withdraw_money(self, user:RegisterUser, value: float):
         with Session(engine) as session:
            withdraw = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if withdraw:
                withdraw.balance -= value
                session.add(withdraw)
                session.commit()


    
    
    
    
    
    
    
    def transfer(self, user:RegisterUser, cpf, value):

        with Session(engine) as session:
            query_balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if query_balance:
                if query_balance.balance >= value:
                    send_money = query_target_user(cpf, value)

                    if send_money is True:
                        query_balance.balance -= value
                    
                    session.add(query_balance)
                    session.commit()
                    return 'Transferência concluída'
                else:
                    return 'Saldo insuficiente'
            
            

       
        
