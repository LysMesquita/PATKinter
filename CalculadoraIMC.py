from tkinter import *
from tkinter import ttk

def calcular_imc(*args):
    try:
        altura = float(altura_var.get())  # Altura em metros
        peso = float(peso_var.get())  # Peso em kg
        imc = peso / (altura ** 2)  # Cálculo do IMC
        resultado_imc.set(f"{imc:.2f}")  # Mostra o resultado com 2 casas decimais
    except ValueError:
        pass

# Criando janela TK
root = Tk()
root.title("Calculadora de IMC")

# Criando o container (nossa "div")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variáveis
altura_var = StringVar()  # Variável da altura
peso_var = StringVar()  # Variável do peso
resultado_imc = StringVar()   # Variável do resultado

# Entrada de altura
ttk.Label(mainframe, text="Altura (em metros e cm)").grid(column=2, row=1, sticky=W)
entrada_altura = ttk.Entry(mainframe, width=7, textvariable=altura_var)
entrada_altura.grid(column=1, row=1, sticky=(W, E))

# Entrada de peso
ttk.Label(mainframe, text="Peso (em Kg)").grid(column=2, row=2, sticky=W)
entrada_peso = ttk.Entry(mainframe, width=7, textvariable=peso_var)
entrada_peso.grid(column=1, row=2, sticky=(W, E))

# Exibição do resultado do IMC
ttk.Label(mainframe, text="Resultado:").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=resultado_imc).grid(column=4, row=2, sticky=(W, E))

# Botão para calcular
ttk.Button(mainframe, text="Calcular", command=calcular_imc).grid(column=4, row=3, sticky=E)

# Configuração de espaçamento entre os widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Foco na entrada de altura
entrada_altura.focus()

# Bind para ao pressionar Enter calcular
root.bind("<Return>", calcular_imc)

# Loop principal da interface (mantém janela aberta, se o loop for interrompido a janela fecha)
root.mainloop()
