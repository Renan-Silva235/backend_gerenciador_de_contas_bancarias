from .base_top_level import BaseTopLevel
from tkinter import ttk
from backend.entities.transaction import Transaction
from backend.format.custom_messagebox import custom_messagebox
from backend.format.custom_message_askyesno import custom_askyesno


class DepositWindow(BaseTopLevel):
    def __init__(self, parent):
        super().__init__(title='Depósito')
        self.parent = parent
        self.class_transaction = Transaction()
        self.create_widgets()



    def create_widgets(self):
        self.deposit_introduce = ttk.Label(self, text='DEPÓSITOS', font=('Ariael', 25))
        self.deposit_introduce.pack(pady=10)


        self.deposit_label = ttk.Label(self, text='Quanto você deseja depositar:', font=('Ariael', 16))
        self.deposit_label.pack(pady=10)
        self.deposit_entry = ttk.Entry(self, font=('Arial', 16))
        self.deposit_entry.pack(pady=10)


        self.deposit_button = ttk.Button(self, text='Depositar', command=self.deposit_money)
        self.deposit_button.pack(pady=10)

        self.cancel_button = ttk.Button(self, text='Cancelar', command=self.cancel)
        self.cancel_button.pack(pady=10)




    def deposit_money(self):
        get_deposit = self.deposit_entry.get()

        if not get_deposit:
            custom_messagebox(self, 'Error', 'Campo inválido')
            return


        confirmation = custom_askyesno(self,
            'Confirmação',
            f'Deseja depositar R$ {get_deposit}'
        )


        if confirmation:
            deposited = self.class_transaction.deposit(self.parent.user, get_deposit)

            if deposited:
                custom_messagebox(self, 'Sucesso', 'Depósito realizado com sucesso.')

            self.destroy()

        if self.parent:
            self.parent.deiconify()


    def cancel(self):
        self.destroy()

        if self.parent:
            self.parent.deiconify()        

        