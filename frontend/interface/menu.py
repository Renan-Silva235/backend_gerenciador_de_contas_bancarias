from .base_window import BaseWindow
from tkinter import ttk, messagebox
from backend.entities.user import User
from .service_window import ServicesWindow
from backend.format.format_cpf import format_cpf_entry


class MainMenu(BaseWindow):
    def __init__(self):
        super().__init__(title='Login')
        self.user = User()
        self.create_widgets()


    def create_widgets(self):

        
        self.label = ttk.Label(self, text='Bem-Vindo ao Banco-Libras', font=('Arial', 30), background='#C0C0C0')
        self.label.pack(pady=20)

        self.label2 = ttk.Label(self, text='Conecte suas contas, Centralize sua vida financeira em um só lugar.', font=("Arial", 16), background='#C0C0C0')
        self.label2.pack(pady=20)
        
        
        self.cpf_label = ttk.Label(self, text="CPF:", font=("Arial", 16), background='#C0C0C0')
        self.cpf_label.pack(pady=10)
        self.cpf_entry = ttk.Entry(self, font=("Arial", 16))
        self.cpf_entry.pack(pady=10)
        self.cpf_entry.bind('<KeyRelease>', lambda event: format_cpf_entry(self.cpf_entry))
        
        self.password_label = ttk.Label(self, text="Senha:", font=("Arial", 16), background='#C0C0C0')
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
            messagebox.showerror('Erro', 'preencha todos os campos')
            return
        
        user = self.user.login(cpf, password)

        if user:
            messagebox.showinfo('Sucesso', 'Login bem-sucedido')
            self.withdraw()
            service_window = ServicesWindow(user)  
            service_window.mainloop()
        else:
            messagebox.showinfo('Erro', 'Login ou senha inválidos')

    def register_count(self):
        from .register_window import RegisterWindow
        self.iconify()
        register_window = RegisterWindow(self)
        register_window.mainloop()
    
           
       

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()