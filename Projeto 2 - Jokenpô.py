import time
import random
jogar = True
while jogar == True:
    hisoka = 0
    illumi = 0
    chrollo = 0
    Pedra = 'PE'
    Papel = 'PA'
    Tesoura = 'TE'
    netero = 0

    ging = input('Vamos jogar Jokenpô! \nDigite seu nickname:')
    hunter = int(input('Digite quantas rodadas você quer jogar!'))
    # while hunter != int:
    #     print('Por favor, digite um número válido.')
    #     hunter = int(input('Digite quantas rodadas você quer jogar!'))

    print('Use "PE" para Pedra, "PA" para Papel, e "TE" para Tesoura.')
    time.sleep(1)

    for nen in range(hunter):
        print('Vamos lá! Faça sua escolha!!\nPE - Pedra\nPA - Papel\nTe - Tesoura')
        print()
        time.sleep(0.3)
        print('Quando eu disser já!')
        time.sleep(0.2)
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        gon = input('JÁ!!').upper()
        killua = random.randint(1,3)

        if gon == Pedra:
            print('Você escolheu PEDRA!')
        elif gon == Papel:
            print('Você escolheu PAPEL!')
        elif gon == Tesoura:
            print('Você escolheu TESOURA!')
        # while not gon == Pedra:
        #     print('Erro. Verifique sua escolha e tente novamente.')
        #     gon = input('Vamos lá! Faça sua escolha!!\nPE - Pedra\nPA - Papel\nTe - Tesoura\nDigite sua escolha abaixo:\n').upper()
        # while not gon == Papel:
        #     print('Erro. Verifique sua escolha e tente novamente.')
        #     gon = input('Vamos lá! Faça sua escolha!!\nPE - Pedra\nPA - Papel\nTe - Tesoura\nDigite sua escolha abaixo:\n').upper()
        # while not gon == Tesoura:
        #     print('Erro. Verifique sua escolha e tente novamente.')
        #     gon = input('Vamos lá! Faça sua escolha!!\nPE - Pedra\nPA - Papel\nTe - Tesoura\nDigite sua escolha abaixo:\n').upper()



        if killua == 1:
            print('Eu escolhi PEDRA!')
            killua = Pedra
        elif killua == 2:
            print('Eu escolhi PAPEL!')
            killua = Papel
        elif killua == 3:
            print('Eu escolhi TESOURA!')
            killua = Tesoura

        if gon == killua:
            print('Empatamos!! Te enfrentar é realmente desafiador!')
            chrollo += 1
        elif gon == Pedra and killua == Papel:
            print('Embrulhado!! Eu venci essa!')
            illumi += 1
        elif gon == Pedra and killua == Tesoura:
            print('Você venceu! Só de imaginar ser esmagado por uma pedra...')
            hisoka += 1
        elif gon == Papel and killua == Pedra:
            print('Você venceu essa!! Será que fui óbvio demais??')
            hisoka += 1
        elif gon == Papel and killua == Tesoura:
            print('Te cortei!! Vitória pra mim!!')
            illumi += 1
        elif gon == Tesoura and killua == Papel:
            print('Você ganhou... Tem certeza de que não está roubando, né?')
            hisoka += 1
        elif gon == Tesoura and killua == Pedra:
            print('Quebrei sua tesoura! Parece que venci, não é?')
            illumi += 1

        
        

        netero += 1
        if netero == hunter:
            pass
        else:
            time.sleep(1)
            print('Próxima rodada...')
            time.sleep(1.2)

    print('Muito obrigado pelo jogo!')
    print()
    print(f'Vamos ao placar!\n\n\nJogador 1: {ging}\nVitórias: {hisoka}\nDerrotas: {illumi}\nEmpates: {chrollo}\n\n\nJogador 2: CPU\nVitórias: {illumi}\nDerrotas: {hisoka}\nEmpates: {chrollo}')



    resposta = input('Deseja jogar novamente?\nUtilize "S" para Sim.\nUtilize "N" para Não.').upper()
    if resposta == 'S':
        pass
    if resposta == 'N':
        jogar = False
    else:
        while resposta != 'S' and resposta != 'N':
            print('Não entendemos sua resposta. Tente de novo:')
            resposta = input('Deseja jogar novamente?\nUtilize "S" para Sim.\nUtilize "N" para Não.').upper()




        
            


        

