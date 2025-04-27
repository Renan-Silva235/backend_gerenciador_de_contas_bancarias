from .base_top_level import BaseTopLevel
from tkinter import ttk, messagebox
from backend.entities.transaction import Transaction




class DepositWindow(BaseTopLevel):
    def __init__(self, parent):
        super().__init__(title='Depósito')
        self.parent = parent
        self.class_transaction = Transaction()
        self.create_widgets()



    def create_widgets(self):
        self.deposit_introduce = ttk.Label(self, text='DEPÓSITOS', font=('Ariael', 25), background='#C0C0C0')
        self.deposit_introduce.pack(padx=10)


        self.deposit_label = ttk.Label(self, text='Quanto você deseja depositar:', font=('Ariael', 16), background='#C0C0C0')
        self.deposit_label.pack(padx=10)
        self.deposit_entry = ttk.Entry(self, font=('Arial', 16))
        self.deposit_entry.pack(padx=10)


        self.deposit_button = ttk.Button(self, text='Depositar', command=self.deposit_money)
        self.deposit_button.pack(padx=10)

        self.cancel_button = ttk.Button(self, text='Cancelar', command=self.cancel)
        self.cancel_button.pack(padx=10)




    def deposit_money(self):
        get_deposit = self.deposit_entry.get()

        if not get_deposit:
            messagebox.showerror('Error', 'Campo inválido', parent=self)



        confirmation = messagebox.askyesno(
            'Confirmação',
            f'Deseja depositar R$ {get_deposit}', parent=self
        )


        if confirmation:
            deposited = self.class_transaction.deposit(self.parent.user, get_deposit)

            if deposited:
                messagebox.showinfo('Sucesso', 'Depósito realizado com sucesso.', parent=self)

            self.destroy()

        if self.parent:
            self.parent.deiconify()


    def cancel(self):
        self.destroy()

        if self.parent:
            self.parent.deiconify()        

        