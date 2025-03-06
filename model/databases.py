from sqlmodel import SQLModel, Field, create_engine
from pydantic import EmailStr


class Users(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=30)
    cpf: str = Field(max_length=11)
    email: EmailStr = Field()
    password: str = Field(max_length=4)


sqlite_file_name = 'model/databases.db'
connection_string = f'sqlite:///{sqlite_file_name}'

engine = create_engine(connection_string, echo=True)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)