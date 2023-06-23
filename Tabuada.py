numTabuada = int(input("Digite o numéro para ver sua tabuada: \n"))
numMult = int(input("Digite o numero até quando {} será multiplicado: \n".format(numTabuada)))

print("="*13)

for i in range(1,numMult+1):
    print("{} x {} = {}".format(numTabuada, i, numTabuada * i))

print("="*13)