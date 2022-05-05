import random

#11
def abrir_arquivo() -> str:
    with open('./arquivos/palavras.txt', 'r') as palavras:
        todas_palavras = palavras.read()
        
    lista_palavras = todas_palavras.split('\n')

    return random.choice(lista_palavras)

def jogar(palavra: str) -> None:
    palavra = palavra.lower()
    qtd_palavras = list('_' * len(palavra))
    erros = 0
    while True:
        print(' '.join(qtd_palavras))
        letra = input('Digite uma letra: ')
        
        letras_achadas = 0
        for l in range(len(palavra)):
            if letra == palavra[l]:
                qtd_palavras[l] = f'{letra} '
                letras_achadas +=1
        
        if letras_achadas == 0:
            erros+=1
            if erros == 6:
                print('Voce Morreu')
                break
            print(f'Você errou pela {erros}ª vez. Tente de novo!')
            
        if '_' not in qtd_palavras:
            print(' '.join(qtd_palavras))
            print('Parabéns, vc terminou')
            break
            
if __name__:
    palavra = abrir_arquivo()
    jogar(palavra)