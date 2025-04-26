from tkinter import ttk, messagebox
from ..interface.base_top_level import BaseTopLevel
from backend.entities.transaction import Transaction
from backend.query.query_target_user import query_target_user
from backend.format.format_cpf import format_cpf_entry


class TransactionWindow(BaseTopLevel):
    def __init__(self, parent):
        super().__init__(title='Transferência')
        self.parent = parent
        self.create_widgets()
        self.class_transfer = Transaction()

    def create_widgets(self):
        self.label = ttk.Label(self, text='Área de transferência', font=('Arial', 18))
        self.label.pack(pady=20)

        self.cpf_label = ttk.Label(self, text='CPF do destinatário:', font=('Arial', 16))
        self.cpf_label.pack(pady=10)
        self.cpf_entry = ttk.Entry(self, font=('Arial', 16))
        self.cpf_entry.pack(pady=10)
        self.cpf_entry.bind('<KeyRelease>', lambda event: format_cpf_entry(self.cpf_entry))


        self.amount_label = ttk.Label(self, text='Valor da transferência:', font=('Arial', 16))
        self.amount_label.pack(pady=10)
        self.amount_entry = ttk.Entry(self, font=('Arial', 16))
        self.amount_entry.pack(pady=10)


        self.transfer_button = ttk.Button(self, text='Transferir', command=self.transfer)
        self.transfer_button.pack(pady=20)
        self.cancel_button = ttk.Button(self, text='Cancelar', command=self.destroy)
        self.cancel_button.pack(pady=20)

    def transfer(self):
        get_cpf = self.cpf_entry.get()
        get_amount = self.amount_entry.get()

        if not get_cpf or not get_amount:   
            messagebox.showerror('Transferência', 'Por favor, insira um valor para a transferência.')
            return

        try:
            

            # Obter o nome do destinatário sem realizar a transferência
            recipient_name = query_target_user(get_cpf)

            if recipient_name is False:
                messagebox.showerror('Transferência', 'CPF do destinatário inválido.')
                return

            # Confirmação com o nome do destinatário
            confirmation = messagebox.askyesno(
                'Confirmação', 
                f'Transferir R$ {get_amount} para {recipient_name.name}, \n '
                  f'cpf: ********{recipient_name.cpf[10:]}', parent=self
            )

            if confirmation:
                # Realizar a transferência após a confirmação
                transaction_result = self.class_transfer.transfer(self.parent.user, get_cpf, get_amount)

                if transaction_result == 'Transferência concluída':
                    messagebox.showinfo('Transferência', 'Transferência realizada com sucesso!', parent=self)
                    self.destroy()
                    self.parent.deiconify()
                else:
                    messagebox.showerror('Transferência', transaction_result)
        except Exception as error:
            messagebox.showerror('Transferência', f'Ocorreu um erro: {error}')
            return
