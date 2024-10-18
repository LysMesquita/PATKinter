from tkinter import *
from tkinter import ttk
import string
import random

def GerarSenha():
    tamanho = 8
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    senha_var.set(senha) #vai "inputar" minha senha na senha_var

root = Tk()
root.title("Gerador de senhas alfanuméricas")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#onde vai ficar alocado
senha_var = StringVar()

label = ttk.Label(mainframe, text="Clique no botão para gerar uma senha (pseudo)aleatória")
label.grid(column=2, row=1, sticky=(W, E))

senha_entry = ttk.Entry(mainframe, width=4, textvariable=senha_var)
senha_entry.grid(column=2, row=2, sticky=(W, E))

botao = ttk.Button(mainframe, width=4, text="Gerar senha", command=GerarSenha)
botao.grid(column=2, row=3, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
