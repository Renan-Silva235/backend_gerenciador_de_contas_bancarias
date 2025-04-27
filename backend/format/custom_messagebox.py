import tkinter as tk
from tkinter import ttk


def custom_messagebox(parent, title='mensagem', message='mensagem exibida'):
    popup = tk.Toplevel(parent)
    popup.title(title)
    popup.geometry('390x150')
    popup.configure(background='#800000')
    popup.resizable(False, False)
    popup.attributes('-topmost', 1)

    label = ttk.Label(popup, text=message, font=('Arial', 14))
    label.pack(pady=20)


    button = ttk.Button(popup, text='OK', command=popup.destroy)
    button.pack(pady=10)

    popup.update_idletasks()

    position_x = parent.winfo_x() + (parent.winfo_width() // 2) - (popup.winfo_width() // 2)
    position_y = parent.winfo_y() + (parent.winfo_height() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f'+{position_x}+{position_y}')

    popup.grab_set()
    popup.wait_window(popup)