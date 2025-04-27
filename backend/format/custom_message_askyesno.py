import tkinter as tk
from tkinter import ttk 


def custom_askyesno(parent, title='Confirmação', question='Deseja continuar?'):
    popup = tk.Toplevel(parent)
    popup.title(title)
    popup.geometry('400x150')
    popup.configure(background='#800000')
    popup.resizable(False, False)
    popup.attributes('-topmost', 1)

    label = ttk.Label(popup, text=question, font=('Arial', 14))
    label.pack(pady=20)

    response = {'answer': None}

    def on_yes():
        response['answer'] = True
        popup.destroy()
    
    
    def on_no():
        response['answer'] = False
        popup.destroy()


    frame = tk.Frame(popup, background='#800000')
    frame.pack()

    yes_button = ttk.Button(frame, text='Sim', command=on_yes)
    yes_button.grid(row=0, column=0, padx=10)
    
    no_button = ttk.Button(frame, text='Não', command=on_no)
    no_button.grid(row=0, column=1, padx=10)

    popup.update_idletasks()
    position_x = parent.winfo_x() + (parent.winfo_width() // 2) - (popup.winfo_width() // 2)
    position_y = parent.winfo_y() + (parent.winfo_height() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{position_x}+{position_y}")    

    popup.grab_set()
    parent.wait_window(popup)


    return response['answer']
    

