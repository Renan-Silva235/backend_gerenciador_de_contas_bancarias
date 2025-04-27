from tkinter import ttk, Toplevel

class BaseTopLevel(Toplevel):
    def __init__(self, title='Painel do usuário', width=1010, height=900):
        super().__init__()
        self.title(title)

        self.window_width = width
        self.window_height = height

        # Coordenadas para centralizar a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_x = (screen_width - self.window_width) // 2
        position_y = (screen_height - self.window_height) // 2

        self.geometry(f'{self.window_width}x{self.window_height}+{position_x}+{position_y}')
        self.resizable(False, False)
        self.attributes('-topmost', 1)
        self.configure(background='#C0C0C0')

        # Estilo para botões
        self.style = ttk.Style()
        self.style.configure('tButton', background='000000', font=('Arial', 20))

        self.update_idletasks()