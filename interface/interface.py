import tkinter as tk

root = tk.Tk()
root.title('Banco Libras')

# altura e largura da janela
window_width = 1010
window_height = 900

# coordenada da minha tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')


root.resizable(False, False)

root.attributes('-topmost', 1)


try:
    photo = tk.PhotoImage(file='~/projetos/gerenciador_contas_bancarias/interface/image/icon.png')
    root.iconphoto(False, photo)
except tk.TclError:
    print('icon file not found')

root.mainloop()