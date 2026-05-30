import random

pontosRecebidos: int = 0

def IniciarJogo():

    numeroAleatorio: int = random.randrange(1,50)

    contador: int = 5
    
    global pontosRecebidos
    

    while contador > 0:

        numeroEscolhido = int(input("Escolha um número de 1 a 50: "))

        if numeroEscolhido != numeroAleatorio and contador > 1:

            print("Numero Incorreto...\n")

            contador = contador - 1

            print(f"Tentativas Restantes {contador}\n")

            if numeroEscolhido > numeroAleatorio:

                print("Tente Um Número Menor\n")
            
            else:

                print("Tente Um Número Maior.\n")
        
        elif numeroEscolhido != numeroAleatorio and contador == 1:

            print(f"Número Incorreto Você Não Tem Mais Tentativas")

            print("--- FIM DE JOGO ---\n")
            contador = contador - 1
        
        else:

            print("Parabéns Você Acertou !!!\n")

            pontosRecebidos = pontosRecebidos + 100
            
            
            break
    
    
def VerPontuacao():

    
    print(f"Total De Pontos Atuais {pontosRecebidos} ")   
     
def Menu():

    while True:

        opcao = str(input('''Selecione uma Opção
                            \nA - Iniciar Jogo
                            \nB - Ver Pontuação
                            \nX - Fechar
                            \n --> ''')).upper()
        
        match opcao:

            case "A":

                IniciarJogo()
            
            case "B":

                VerPontuacao()
            
            case "X":
                print("Encerrando...")
                break
            
            case _:
                print("Opção Inválida...\n")


Menu()

