
dinheiro = float(input("Quanto dinheiro você tem na carteira? \n"))

moeda = int(input("Qual moeda você que converte o real? \n "
          "1-Dolar(USD) \n 2-Euro\n 3-Yene\n"
                  "Digite o número corespondente a moeda: "))

def case1():
    print("Com R${} você pode compra US${:.2f}".format(dinheiro, dinheiro/4.77))

def case2():
    print("Com R${} você pode compra €{:.2f}".format(dinheiro, dinheiro / 5.22))

def case3():
    print("Com R${} você pode compra JP¥{:.2f}".format(dinheiro, dinheiro * 30))
switch = {
    1: case1,
    2: case2,
    3: case3
}

switch[moeda]()