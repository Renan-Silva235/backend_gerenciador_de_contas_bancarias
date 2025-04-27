from .base_top_level import BaseTopLevel
from tkinter import ttk, messagebox
from backend.entities.transaction import Transaction


class WithdrawWindow(BaseTopLevel):
    def __init__(self, parent):
        super().__init__(title='Saque')
        self.parent = parent
        self.create_widgets()


    def create_widgets(self):
        self.label_introduce = ttk.Label(self, text='Sacar:', font=('Arial', 25), background='#C0C0C0')
        self.label_introduce.pack(pady=10)

        self.withdraw_label = ttk.Label(self, text='Quanto você deseja sacar?', font=('Arial', 16), background='#C0C0C0')
        self.withdraw_label.pack(padx=10)
        self.withdraw_entry = ttk.Entry(self, font=('Arial', 16))
        self.withdraw_entry.pack(padx=10)

        self.button_withdraw = ttk.Button(self, text='Sacar', command=self.withdraw_cash)
        self.button_withdraw.pack(padx=10)

        self.button_cancel = ttk.Button(self, text='voltar', command=self.back)
        self.button_cancel.pack(padx=10)

    def withdraw_cash(self):
        get_amount = self.withdraw_entry.get()
        class_transaction = Transaction()

        confirmation = messagebox.askyesno(
            'Confirmação',
            f'Você realmente deseja sacar R$ {get_amount}', parent=self
        )


        if confirmation:

            withdraw_money = class_transaction.withdraw_money(self.parent.user, get_amount)

            if withdraw_money == False:
                messagebox.showerror('Error', 'Saldo insuficiente', parent=self)
            else:
                messagebox.showinfo('Sucesso', 'Valor sacado com sucesso', parent=self)
                self.destroy()

                if self.parent:
                    self.parent.deiconify()
    
    def back(self):
        self.destroy()
        if self.parent:
            self.parent.deiconify()

            


    
