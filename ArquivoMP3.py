from tkinter import Tk, Button, filedialog
from playsound import playsound

def selecionar_arquivo():
    # Exibe a caixa de diálogo de seleção de arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos MP3", "*.mp3")])

    if arquivo:
        # Reproduz o arquivo MP3
        playsound(arquivo)

# Cria a janela principal
janela = Tk()

# Cria o botão
botao = Button(janela, text="Selecionar MP3", command=selecionar_arquivo)
botao.pack()

# Inicia o loop principal da janela
janela.mainloop()