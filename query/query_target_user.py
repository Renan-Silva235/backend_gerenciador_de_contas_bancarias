from model.databases import RegisterUser, TransactionModel, engine
from sqlmodel import Session

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