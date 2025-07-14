palavraEscolhida = ["b","o","l","a"]
palavra = []
tentativas = 6
forca = ["O","|","/","/","/","/"]

for i in range (100):
    letra = input(f"Informe uma letra para saber se tem na palavra: ")
    if letra in palavraEscolhida:
        palavra.append(letra)
        print(palavra)
    elif letra != palavraEscolhida[0]:
        print(f"Errado. Você tem {tentativas} tentativas ")
        tentativas-=1
    elif palavraEscolhida == palavra:
        print("Acertou!")
        break
    elif tentativas == 0:
        print("Morreu niuba")
        break
#     print(i)

# if letra in palavraEscolhida:
