def imprimeNome(nome):
     print(f"Nome: {nome}")
 
def solicitarNome():
     nome = input("Digite seu nome: ")
     return nome


def gerarArvore(numero):
    resultado = ""
    for i in range(1, numero + 1):
        for j in range(i):
            resultado += f"{i} " 
        resultado += "\n"  
    return resultado