notas = [0.0,0.0,0.0,0.0,0.0]
soma = 0
alunosAcima = 0

for i in range(len(notas)):
    notas [i] = float(input(f"informe a nota {i+1}: "))

for i in range(len(notas)):
    soma += notas[i] 
media = soma / len(notas)

for i in range(len(notas)):
    if notas[i] > media:
        alunosAcima += 1

print(f"A media geral da turma foi: {media}. E a quantidade de alunos que ficaram acima foi {alunosAcima}")