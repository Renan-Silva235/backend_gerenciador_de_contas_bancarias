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
                return balance.balance
                
            
            


    def withdraw_money(self, user:RegisterUser, value: str):
         with Session(engine) as session:
            query_balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()

            if query_balance:
                if query_balance.balance >= Decimal(value):
                    query_balance.balance -= Decimal(value).quantize(Decimal('0.01'))
                    session.add(query_balance)
                    session.commit()
                else:
                    return False

    
    def transfer(self, user:RegisterUser, cpf, value: str):

        with Session(engine) as session:
            query_balance = session.query(TransactionModel).filter(TransactionModel.user_id == user.user_id).first()
            target_user = query_target_user(cpf)




            if query_balance:
                if query_balance.balance >= Decimal(value):
                    query_balance.balance -= Decimal(value).quantize(Decimal('0.01'))
                    

                    if target_user is False:
                        return 'CPF do destinatário inválido'
                    else:
                        send_for_target = session.query(TransactionModel).filter(TransactionModel.user_id == target_user.user_id).first()
                        
                        if send_for_target:
                            send_for_target.balance += Decimal(value).quantize(Decimal('0.01'))
                            session.add(send_for_target)
                            session.commit()
                    # Verifica se o CPF é igual ao do usuário atual
                    
                    session.add(query_balance)
                    session.commit()        
                    return 'Transferência concluída'
                else:
                    return 'Saldo insuficiente'
            
            

       
        
