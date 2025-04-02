from sqlmodel import Session
from model.databases import RegisterUser, engine
from validate_docbr import CPF


class ValidCpf(CPF):

    def verify_cpf_exist(self, cpf):
        with Session(engine) as session:
            verify_cpf_exist = session.query(RegisterUser).filter(RegisterUser.cpf == cpf).first()

            if verify_cpf_exist:
                raise Exception('Parece que já existe uma conta com esse CPF')
            
        return False
                
            



    def verify_cpf_is_valid(self,cpf):
        if CPF().validate(cpf):
            return cpf
        else:
            raise ValueError('CPF inválido')
        




def valid_cpf(cpf):
    cpf_veryfied = ValidCpf().verify_cpf_exist(cpf)
    cpf_valided = ValidCpf().verify_cpf_is_valid(cpf)
    return cpf_veryfied or cpf_valided




    






