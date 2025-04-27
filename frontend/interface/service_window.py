from tkinter import ttk
from ..interface.base_top_level import BaseTopLevel
from .transaction_window import TransactionWindow
from backend.entities.transaction import Transaction
from .withdraw_window import WithdrawWindow
from .deposit_window import DepositWindow


class ServicesWindow(BaseTopLevel):
    def __init__(self, user):
        super().__init__(title='Painel do usuário')
        self.user = user
        transaction = Transaction()
        self.user_balance = transaction.get_balance(user)
        self.create_widgets()
        


    def create_widgets(self):
        self.label = ttk.Label(self, text=f'Olá {self.user.name}, seja bem vindo(a) ao Banco Libras', font=('Arial', 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=20, sticky='n')

        self.logout_button = ttk.Button(self, text='Sair', command=self.logout, width=6)
        self.logout_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
        
        self.label_balance = ttk.Label(self, text=f'Saldo: R$ {self.user_balance}', font=('Arial', 16))
        self.label_balance.grid(row=1, column=0, columnspan=3, pady=10)
        self.label_balance.grid_remove()

        self.show_balance = False
        self.button_balance = ttk.Button(self, text='Mostrar saldo', command=self.toggle_balance)
        self.button_balance.grid(row=2, column=0, columnspan=3, pady=10)

        # Frame para centralizar os botões de ação
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=3, column=0, columnspan=3, pady=20)

        self.button_transfer = ttk.Button(self.button_frame, text='Transferir', command=self.open_transaction_window)
        self.button_transfer.grid(row=0, column=0, padx=10, pady=10)

        self.button_withdraw = ttk.Button(self.button_frame, text='Saque', command=self.open_withdraw_window)
        self.button_withdraw.grid(row=0, column=1, padx=10, pady=10)

        self.button_deposit = ttk.Button(self.button_frame, text='Depositar', command=self.deposit)
        self.button_deposit.grid(row=0, column=2, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
       

    def open_transaction_window(self):
        self.withdraw()
        transaction_window = TransactionWindow(self)
        transaction_window.mainloop()



    def toggle_balance(self):
        if self.show_balance:
            self.label_balance.grid_remove()
            self.button_balance.config(text='Mostrar saldo')
        else:
            self.label_balance.grid()
            self.button_balance.config(text='Ocultar saldo')
        self.show_balance = not self.show_balance
    
    # Atualizar o saldo após o fechamento da janela
        transaction = Transaction()
        updated_balance = transaction.get_balance(self.user)
        self.label_balance.config(text=f'Saldo: R$ {updated_balance}')


    
    def open_withdraw_window(self):
        self.withdraw()

        withdraw_window = WithdrawWindow(self)
        withdraw_window.mainloop()


    def deposit(self):
        self.withdraw()
        deposit_window = DepositWindow(self)
        deposit_window.mainloop()

    def logout(self):
        self.destroy()
        self.master.deiconify()
