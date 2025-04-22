from backend.model.databases import RegisterUser, TransactionModel, engine
from sqlmodel import Session
from decimal import Decimal

def query_target_user(cpf:str) :
    with Session(engine) as target_session:
        target_user = target_session.query(RegisterUser).filter(RegisterUser.cpf == cpf).first()
        if target_user:
            
            return target_user 
        
        return False
