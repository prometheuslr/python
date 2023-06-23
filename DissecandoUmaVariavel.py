x="s"
a="s"
while(x=="s"):
    texto = input("Digite algo \n")
    print("O tipo primitivo desse valor é " .format(type(texto)) )
    print("So tem espaços? {}" .format(texto.isspace()))
    print("É um número? {}" .format(texto.isnumeric()))
    print("É alfabetico? {}" .format(texto.isalpha()) )
    print("É um alfanúmerico? {}" .format(texto.isalnum()))
    print("Esta em maiúscula? {}".format(texto.isupper()) )
    print("Esta em minúscula? {}".format(texto.islower()) )
    print("Esta capitalizada? {}".format(texto.istitle()) )
    x = str(input("Deseja continuar s/n \n"))
    if(x!= "s" or x!= "n"):
        x="s"
        print("Digite s sim ou n para não ")

