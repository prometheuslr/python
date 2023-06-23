
x = "s"

while (x=="s"):
    metro = float(input("Digite uma medida em metro \n"))
    print("A medida de {}m corresponde" .format(metro))
    print("{}km".format(metro/1000))
    print("{}hm".format(metro/100))
    print("{}dam".format(metro/10))
    print("{}dm".format(metro*10))
    print("{}cm".format(metro*100))
    print("{}mm".format(metro*1000))
    x=input("Deseja continuar s/n \n")