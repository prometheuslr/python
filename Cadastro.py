import tkinter as tk
from tkinter import ttk
import datetime as dt

listaTipo = ["Pá", "Cimento","Brita", "Areia"]
janela = tk.Tk()

#Titulo da janela
janela.title("Cadastro")

labelDescricao = tk.Label(text="Descrição dos materiais")
labelDescricao.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan= 4 )

entryDescricao = tk.Entry()
entryDescricao.grid(row=2, column=0, padx=10, pady=10,sticky="nswe",columnspan=4)

labelTipoUnidade = tk.Label(text="Tipo da unidade do Material")
labelTipoUnidade.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan= 2 )

comboboxSelecionarTipo = ttk.Combobox(values=listaTipo)
comboboxSelecionarTipo.grid(row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan= 2 )

janela.mainloop()