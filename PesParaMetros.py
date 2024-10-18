from tkinter import *
from tkinter import ttk
#import * importa TUDO; (asterisco significa "tudo" em muitos usos da informática)

def calculate (*args):
        try:
                value = float (feet.get()) #ENTRADA 
                #ESSA PARTE PEGA O VALOR, "INSERE" NO "FEET" E CONVERTE A STRING PARA FLOAT 
                result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 #PROCESSAMENTO
                #CONTA PARA CONVERSÃO
                meters.set(result) #SAÍDA 
                #ELE PEGA E "SETA" O RESULTADO NOS METROS (NA VARIAVEL METERS)
        except ValueError:
                pass
        #ELE IMPRIME O ERRO (FUNÇÃO PASS)

        #tudo acima é referente ao comando de converter (converter=) da linha 30

        #criando a janela TK 
        root = Tk()
        #Configurando título do app
        root.title("Pés para metros")

        #criando o container (nossa "div")
        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #variavel para armazenar os dados
        feet = StringVar()

        # nosso input (ttk.Entry) abaixo:
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
        #mainframe "inputa" ele na nossa div
        #o width faz com que ele cresça até 7 pixels. Quando expandirmos a janela ele cresce e trava nesses 7 pixels
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        #localiza essa "parte" no nosso grid (na div). O sticky faz com que ele se expanda ao máximo que puder nas respectivas cardinalidades informadas.
        #precisa de pelo menos 1 (mas podemos definir um limite de pixels como acima)

        meters = StringVar()
        ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) #o Label é o nosso texto (uma espécie de <p>)
        ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W) #quando for só uma cardinalidade no sticky, não precisamos de parenteses a mais

        ttk.Label(mainframe, text="pés").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
                #Ele faz um For por todos os "filhos" do código (como se fossem varias divs em uma classe)
                child.grid_configure(padx=5, pady=5)
                #aqui ele pega as "divs" e configura elas com um espaçamento entre si, horizontalmente e verticalmente de forma respectiva.
                #como se deixassemos uma margem entre os filhos para melhor organização
        feet_entry.focus()
        #para quando entrarmos no app/janela, a área de input ficar com a barrinha piscando
        root.bind("<Return>", calculate)
        #aqui é para o ENTER do teclado funcionarr como o ato de clicar no botão "Calcular"

        #Gerando loop para renderização intermitente.
        root.mainloop()