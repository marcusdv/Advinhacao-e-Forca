import random 


def recomecar():
    quer_jogar = input('Digite 1 para jogar novamente ᕦ(ツ)ᕤ\n>>> ')
    if(quer_jogar == '1'):
        print('Boa sorte desgraçado. ( ͡~ ͜ʖ ͡°)\n')
        jogar()
    else:
        print('Então tá seu bostão. (ツ)╭∩╮\n')

def fim_de_jogo(chute, numero_sorteado, chances):
    acertou = chute == numero_sorteado
    acabou_chances = chances == 1

    if(acertou):
        print('Acertou disgrama!!!!! (👍≖‿‿≖)👍 👍(≖‿‿≖👍)\nEra: ', numero_sorteado)
        return True
    if(acabou_chances):
        print('Perdeu otário. (ㆆ_ㆆ)\nEra:', numero_sorteado)
        return True

def verifica_caractere_inv(chute_string):
    success = False
    while not success:
        try:
            chute_int = int(chute_string) #se não for um número, loopa
            success = True
            return chute_int
        except:
            chute_string = input('Digite números seu imbecil 💪(◡̀_◡́҂)\n>>> ') 

def jogar():
    numero_secreto = 0
    tentativa_int = 0
    numero_secreto = random.randrange(10) + 1
    numero_de_tentativas = 3

    for _ in range(0, 3):

        if(numero_de_tentativas == 3):
            tentativa_string = input('Adivinhe o número que pensei! De 1 a 10?\n>>> ')

        tentativa_int = verifica_caractere_inv(tentativa_string)
        
        if(fim_de_jogo(tentativa_int, numero_secreto, numero_de_tentativas)):
            break

        fora_do_range = tentativa_int > 10 or tentativa_int < 1
        menor = tentativa_int < numero_secreto
        maior = tentativa_int > numero_secreto

        if(fora_do_range):
            tentativa_string = input('Não seja burro, esta escrito de 1 a 10 💪 (•︡益︠•) 👊\n>>> ')
        elif(menor):
            tentativa_string = input('Errou! Chute um número mais alto. ☝ (ツ)\n>>> ')
            numero_de_tentativas -= 1
        elif(maior):
            tentativa_string = input('Errou! Chute um número menor. 👇(ツ)\n>>> ')
            numero_de_tentativas -= 1

    recomecar()

if(__name__ == 'main'):
    jogar()