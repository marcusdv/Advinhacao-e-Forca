import adivinhacao
import forca

def starta_menu():
    opcao = input("""
        Escolha um jogo meu bom. 🤓
        (1) Advinhacao 
        (2) Forca
        
    >>> """)
    inicia_jogo(opcao)

def inicia_jogo(opcao):
    if(opcao == '1'):
        adivinhacao.jogar()
    elif(opcao == '2'):
        forca.jogar()

starta_menu()