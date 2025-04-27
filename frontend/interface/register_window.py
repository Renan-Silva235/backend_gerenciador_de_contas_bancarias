from .base_window import BaseWindow
from tkinter import ttk, messagebox
from backend.entities.user import User
from backend.format.format_cpf import format_cpf_entry
from .base_top_level import BaseTopLevel
from backend.format.custom_messagebox import custom_messagebox

class RegisterWindow(BaseTopLevel):
    def __init__(self, parent):
        super().__init__(title='Cadastro')
        self.parent = parent
        self.user = User()
        self.create_widgets()

    
    
    def create_widgets(self):
        
        self.label = ttk.Label(self, text='Cadastro de Usuário', font=('Arial', 30)) 
        self.label.pack(pady=20)
        
        
        self.label2 = ttk.Label(self, text='Preencha os campos abaixo para criar uma conta.', font=("Arial", 16))
        self.label2.pack(pady=20)
        
        
        
        self.name_label = ttk.Label(self, text='Nome:', font=('Arial', 16))
        self.name_label.pack(pady=10)
        self.name_entry = ttk.Entry(self, font=('Arial', 16))
        self.name_entry.pack(pady=10)
        
        self.cpf_label = ttk.Label(self, text='CPF:', font=('Arial', 16))
        self.cpf_label.pack(pady=10)
        self.cpf_entry = ttk.Entry(self, font=('Arial', 16))
        self.cpf_entry.pack(pady=10)
        self.cpf_entry.bind('<KeyRelease>', lambda event: format_cpf_entry(self.cpf_entry))

        self.email_label = ttk.Label(self, text='Email:', font=('Arial', 16))
        self.email_label.pack(pady=10)
        self.email_entry = ttk.Entry(self, font=('Arial', 16))
        self.email_entry.pack(pady=10)

        self.password_label = ttk.Label(self, text='Senha:', font=('Arial', 16))
        self.password_label.pack(pady=10)
        self.password_entry = ttk.Entry(self, font=('Arial', 16))
        self.password_entry.pack(pady=10)

        self.button = ttk.Button(self, text='Cadatrar', command=self.register_user)
        self.button.pack(pady=10)

        self.cancel_button = ttk.Button(self, text='sair', command=self.exit)
        self.cancel_button.pack(pady=10)
          

        


    def register_user(self):
        name = self.name_entry.get()
        cpf = self.cpf_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not name or not cpf or not email or not password:
            custom_messagebox(self, 'Erro', 'Por favor, preencha todos os campos.')
            return
        
        register = self.user.register_user(name, cpf, email, password)

        if register == 'E-mail-inválido':
            custom_messagebox(self, 'Erro', 'E-mail inválido.')
        elif register == 'senha inválida':
            custom_messagebox(self, 'Erro', 'Senha inválida.')
        elif register == 'cpf inválido':
            custom_messagebox(self, 'Erro', 'CPF inválido.')
        elif register == 'CPF já cadastrado':
            custom_messagebox(self, 'Erro', 'Esse CPF já está cadastrado.')
        else:
            custom_messagebox(self, 'Sucesso', 'Usuário cadastrado com sucesso!')
            self.destroy()
            
            if self.parent:
                self.parent.deiconify()


    def exit(self):
        self.destroy()
        if self.parent:
            self.parent.after(100, self.parent.deiconify)
        
    