from backend.model.databases import RegisterUser, TransactionModel, engine
from sqlmodel import Session
from decimal import Decimal

def query_target_user(cpf:str, value: str):
    with Session(engine) as target_session:
        target_user = target_session.query(RegisterUser).filter(RegisterUser.cpf == cpf).first()

        if target_user:
            target_transaction = target_session.query(TransactionModel).filter(TransactionModel.user_id == target_user.user_id).first()

            if target_transaction:
                target_transaction.balance += Decimal(value).quantize(Decimal('0.01'))
                target_session.add(target_transaction)
                target_session.commit()
                
    return True
