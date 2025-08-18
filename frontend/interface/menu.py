from .base_window import BaseWindow
from tkinter import ttk
from backend.entities.user import User
from .service_window import ServicesWindow
from backend.format.format_cpf import format_cpf_entry
from backend.format.custom_messagebox import custom_messagebox


class MainMenu(BaseWindow):
    def __init__(self):
        super().__init__(title='Login')
        self.user = User()
        self.create_widgets()


    def create_widgets(self):

        
        self.label = ttk.Label(self, text='Bem-Vindo ao Banco-Libras', font=('Arial', 30))
        self.label.pack(pady=20)

        self.label2 = ttk.Label(self, text='Conecte suas contas, Centralize sua vida financeira em um só lugar.', font=("Arial", 16))
        self.label2.pack(pady=20)
        
        
        self.cpf_label = ttk.Label(self, text="CPF:", font=("Arial", 16))
        self.cpf_label.pack(pady=10)
        self.cpf_entry = ttk.Entry(self, font=("Arial", 16))
        self.cpf_entry.pack(pady=10)
        self.cpf_entry.bind('<KeyRelease>', lambda event: format_cpf_entry(self.cpf_entry))
        
        self.password_label = ttk.Label(self, text="Senha:", font=("Arial", 16))
        self.password_label.pack(pady=10)
        self.password_entry = ttk.Entry(self, font=('arial', 16), show='*')
        self.password_entry.pack(pady=10)

        self.login_button = ttk.Button(self, text='Login', command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = ttk.Button(self, text='Criar Conta', command=self.register_count)
        self.register_button.pack(pady=10)


    def login(self):
        cpf = self.cpf_entry.get()
        password = self.password_entry.get()

        if not cpf or not password:
            custom_messagebox(self, 'Erro', 'preencha todos os campos')
            return
        
        user = self.user.login(cpf, password)

        if user:
            custom_messagebox(self, 'Sucesso', 'Login bem-sucedido')
            self.withdraw()
            service_window = ServicesWindow(user)  
            service_window.mainloop()
        else:
            custom_messagebox(self, 'Erro', 'Login ou senha inválidos')

    def register_count(self):
        from .register_window import RegisterWindow
        self.withdraw()
        # Passar a referência correta da janela pai
        register_window = RegisterWindow(parent=self)
        register_window.mainloop()

        
    
def main():
    app = MainMenu()
    app.mainloop()

    if __name__ == "__main__":
        main()