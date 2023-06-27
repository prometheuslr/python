import tkinter as tk
from tkinter import ttk
import datetime as dt

listaTipo = ["Bebida","Limpeza", "Cereais", "Matinais", "Bazar", "Hortfruti"]
listaCodigo=[]
janela = tk.Tk()

#Criar função

def inserirCodigo():
    descricao = entryDescricao.get()
    tipo = comboboxSelecionarTipo.get()
    quantidade = entryQuant.get()
    dataCriacao = dt.datetime.now()
    dataCriacao = dataCriacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(listaCodigo)+1
    codigoStr = "COD-{}".format(codigo)
    listaCodigo.append((codigoStr, descricao, tipo, quantidade, dataCriacao))

#Titulo da janela
janela.title("Cadastro de Produtos")

labelDescricao = tk.Label(text="Nome do Produto")
labelDescricao.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan= 4 )

entryDescricao = tk.Entry()
entryDescricao.grid(row=2, column=0, padx=10, pady=10,sticky="nswe",columnspan=4)

labelTipoUnidade = tk.Label(text="Tipo do Produto")
labelTipoUnidade.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan= 2 )

comboboxSelecionarTipo = ttk.Combobox(values=listaTipo)
comboboxSelecionarTipo.grid(row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan= 2 )

labelQuantidade = tk.Label(text="Quantidade da unidade do Produto")
labelQuantidade.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan= 2 )

entryQuant = tk.Entry()
entryQuant.grid(row=4, column=2, padx=10, pady=10, sticky="nswe", columnspan= 2)

botaoCriarCodigo = tk.Button(text="Criar codigo", command=inserirCodigo)
botaoCriarCodigo.grid(row=5, column=0,  padx=10, pady=10, sticky="nswe", columnspan= 4)
janela.mainloop()



arquivo = open("bdProdutos.txt","a")
x = " ". join(str(i) for i in listaCodigo)
arquivo.writelines(x)
arquivo.close()

