nomes = ["","","","",""]

for i in range(len(nomes)):
    nomes[i] = input(f"Informe o {i+1}º nome: ")

for i in range(len(nomes)):
     print(f"O nome: {nomes[i]} está na posição: {i+1}")

nome = input("Digite um nome para saber se esta na lista: ")
if nome in nomes:
    posicao = nomes.index(nome) + 1
    print(f"O nome {nome} está na lista. Na posição {posicao}")
else:
    print("O nome não está na lista")