from PySimpleGUI import  PySimpleGUI as sg


# Layout
sg.theme("Reddit")
layout=[
    [sg.Text("Usuário"), sg.Input(key="usuario", size=(20,1))],
    [sg.Text("Senha"), sg.Input(key="senha", password_char="*", size=(20,1))],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar")],
    [sg.Button("Cadastrar")]
]


cadastro = [
    [sg.Text("Usuario"),sg.Input(key="usuario", size=(20,1))],
    [sg.Text("Email"), sg.Input(key="email", size=(20,1))],
    [sg.Text("Senha"), sg.Input(key="senha", size=(20,1), password_char="*")],
    [sg.Text("Confirme sua senha "), sg.Input(key="confSenha", size=(20,1), password_char="*")],
    [sg.Button("Cadastrar")],
    [sg.Button("Entrar")]
]
# Janela

janela = sg.Window("Tela de Login", layout)
janelaCadastro = sg.Window("Tela de Cadastro", cadastro)
# Ler os eventos

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores['usuario'] == 'lucas' and valores['senha'] == '12345678':
            print("Login realizado com sucesso")
        else:
            print("Usuario ou Senha incoreta")

    if eventos == "Cadastrar":
        while True:
            eventos, valores = janelaCadastro.read()
            if eventos == sg.WINDOW_CLOSED:
                break

            if eventos == "Cadastrar":
                if ((valores['usuario']== "") or (valores["email"] == "") or (valores["senha"] == "") or (valores["confSenha"] == "")):
                    print("Não é permitito nenhum campo nulo")
                elif ((valores["senha"] != valores["confSenha"]) or (valores["confSenha"] != valores["senha"])):
                    print("Senha não são iguais")
                else:
                    print("Cadastro realizado co sucesso")