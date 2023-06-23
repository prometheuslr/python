import random

aluno = []
numAluno = int(input("Qual é a quantidade de alunos que serão sorteados? \n"))
for i in range(1, numAluno+1):
    nomeAluno = input("Qual é o nome do alunoª:\n")
    aluno.append(nomeAluno)

sorteio = random.choice(aluno)
print("O aluno sortiado foi {}" .format(sorteio))

