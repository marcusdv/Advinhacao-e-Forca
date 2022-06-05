import random
import sys

#testando leitura me arquivos txt
# arquivo = open('./bd/frutas.txt')

# palavras = []
# for linha in arquivo:
#     palavras.append(linha)

# arquivo.close()

def gerar_palavras():
    sys.path.insert(0, './bd')
    import palavras_bd
    return palavras_bd.arr()

def checa_fim_jogo(letras_acertadas):
    if(('_' in letras_acertadas) == False):
        print('Boa cacete! 🤘🤘🤘')
        return True

def bem_vindo():
    print('Bem vindo a forca! 😂😂😂')
    print('Dica: É um animal🤐')

def imprimir_palavra(palavra, numero_chutes, letras_erradas):
    tiro = '😀       🔫'
    if(numero_chutes == 1):
        tiro = '😳      ⁃🔫'
    elif(numero_chutes == 2):
        tiro = '😲    ⁃  🔫'
    elif(numero_chutes == 3):
        tiro = '😨  ⁃    🔫'
    elif(numero_chutes == 4):
        tiro = '😱⁃      🔫'
    elif(numero_chutes == 5):
        tiro = '☠️       🔫'

    print(
        """
        {}                                                      

        {}       

        chutes: {}       
        """
        .format(
            tiro,
            ' '.join(palavra),
            '  '.join(letras_erradas)
        ))

def verifica_caractere_inv(letra_chutada):
    letra_chutada = letra_chutada.lower()
    letra_chutada = letra_chutada.strip()
    success = False
    
    while not success:
        try:
            
            float(letra_chutada) #se der erro em converter, quer dizer que é uma string e está correto.
            letra_chutada = input('Digite uma letra válida. 💪(◡̀_◡́҂)\n>>> ') 
        except:     
            if(len(letra_chutada) > 1):
                letra_chutada = input('Letras demais meu broder (◡̀_◡́)\n>>> ') 
            else:
                success = True
                return letra_chutada

def verifica_letra_repetida(chutada, erradas, acertadas, erros):
            imprimir_palavra(acertadas, erros, erradas)
            chutada = input('Letra já foi chutada amigão, chute outra\n>>> ')
            chutada = verifica_caractere_inv(chutada)
            return chutada

def jogar():
    num_erros = 0
    palavras = gerar_palavras()
    palavra_sorteada = palavras[random.randrange(len(palavras))]
    letras_acertadas = len(palavra_sorteada) * ['_']
    letras_erradas = []

    bem_vindo()
    while(num_erros < 5):
        imprimir_palavra(letras_acertadas, num_erros, letras_erradas)
        if(checa_fim_jogo(letras_acertadas)):
            break

        letra_chutada = input('Chute uma letra.\n>>>')
        letra_chutada = verifica_caractere_inv(letra_chutada)
        while(letra_chutada in letras_erradas or letra_chutada in letras_acertadas):
            letra_chutada = verifica_letra_repetida(letra_chutada, letras_erradas, letras_acertadas, num_erros)

        errou_chute = letra_chutada not in palavra_sorteada
        if(errou_chute):
            letras_erradas.append(letra_chutada)
            num_erros += 1

        for idx, letra in enumerate(palavra_sorteada):
            acertou = letra_chutada == letra
            if(acertou):
                letras_acertadas[idx] = letra

        
                

    if(num_erros == 5):
        imprimir_palavra(letras_acertadas, num_erros, letras_erradas)
        print('Perdeu feão!🤢 a palavra era:', palavra_sorteada.upper())
        print('-----------------------------------------------')

    recomecar()
    
def recomecar():
    quer_jogar = input('Digite 1 para jogar novamente ᕦ(ツ)ᕤ\n>>> ')
    if(quer_jogar == '1'):
        print('Boa sorte desgraçado. ( ͡~ ͜ʖ ͡°)\n')
        jogar()
    else:
        print('Então tá seu bostão. (ツ)╭∩╮\n')

if(__name__ == "__main__"):
    jogar()