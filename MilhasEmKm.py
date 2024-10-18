from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(miles.get())  # ENTRADA
        result = int(1.60934 * value * 10000.0 + 0.5)/10000.0  # PROCESSAMENTO
        km.set(result)  # SAÍDA
    except ValueError:
        pass

# Criando janela TK
root = Tk()
root.title("Milhas para Km")

# Criando o container (nossa "div" no python)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

miles = StringVar()  # Variável de ENTRADA
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W, E))

km = StringVar()  # Variável de SAÍDA
ttk.Label(mainframe, textvariable=km).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

# Configurando os labels
ttk.Label(mainframe, text="milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="km").grid(column=3, row=2, sticky=W)

# Espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

miles_entry.focus()  # Foco na entrada de milhas
root.bind("<Return>", calculate)  # Enter no teclado também calcula

# Loop principal da interface
root.mainloop()
