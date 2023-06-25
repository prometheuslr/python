import random

print("{}".format("="*20))
print("Sorteio Digital")
print("{}".format("="*20))

primNumero = int(input("Digite o primerio número do sorteio:\n"))
ultNumero = int(input("Digite o ultimo número do sorteio:\n"))
quantidadeNumeroSorteado = int(input("Qual é a quantidade de números sorteados\n"))
vezesSorteio = int(input("Quantas vezes vocÊ quer que o sorteio ocorra:\n"))

conjuntoNumero = list(range(primNumero, ultNumero + 1))

print("{}".format("=" * (quantidadeNumeroSorteado ** 2 + 5)))

linha = 10
for i in range(0, len(conjuntoNumero), linha):
    print(conjuntoNumero[i:i+linha])

print("{}".format("=" * (quantidadeNumeroSorteado ** 2 + 5 )))

x = 0
for i in range(1,vezesSorteio+1):
    x = x+1
    y = random.sample(conjuntoNumero,quantidadeNumeroSorteado)

    print("{} - {}".format(x, y))
    print("{}".format("=" * (quantidadeNumeroSorteado ** 2)))


