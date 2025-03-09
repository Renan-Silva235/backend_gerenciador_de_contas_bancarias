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


    def transfer(self, user:RegisterUser, cpf, value):



        
        def query_target_user(cpf:str, value):
            with Session(engine) as target_session:
                target_user = target_session.query(RegisterUser).filter(RegisterUser.cpf == cpf).first()

                if target_user:
                    target_transaction = target_session.query(TransactionModel).filter(TransactionModel.user_id == target_user.user_id).first()

                    if target_transaction:
                        target_transaction.balance += value
                        target_session.add(target_transaction)
                        target_session.commit()
                        
            return True
                



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
            
            

       
        
