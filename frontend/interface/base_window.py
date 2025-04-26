import tkinter as tk
from tkinter import ttk
import os

class BaseWindow(tk.Tk):
    def __init__(self, title='Banco-Libras', width=1010, height=900):
        super().__init__()    
        self.title(title)

        self.window_width = width
        self.window_height = height

        # coordenada da minha tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()


        position_x = (screen_width - self.window_width) // 2
        position_y = (screen_height - self.window_height) // 2

        self.geometry(f'{self.window_width}x{self.window_height}+{position_x}+{position_y}')


        self.resizable(False, False)

        self.attributes('-topmost', 1)
        self.configure(background='#C0C0C0')
        

#         varificar o sistema operacional
        # if os.name == 'nt':
        #     icon_path = 'frontend/interface/image/favicon.ico'
        #     self.iconbitmap(icon_path)
        # else:
        #     icon_path = '/home/rsr/Projetos/gerenciador_contas_bancarias/frontend/interface/image/emblema.png'
        #     self.icon = tk.PhotoImage(file=icon_path)
        #     self.tk.call('wm', 'iconphoto', self._w, self.icon)


        self.style = ttk.Style()
        self.style.configure('tButton', background='000000', font=('Arial', 20), )

       
        self.update_idletasks()  # Atualiza o layout para obter as dimensões corretas



