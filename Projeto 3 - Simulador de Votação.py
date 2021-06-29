Jacaré = 0
Sapo = 0
Flamingo = 0
Nulo = 0
Branco = 0
Sistema = True

def autoriza_voto(ano):

 if ano == 2004 or ano == 2005 or ano < 1951:
        pergunta = input('O seu voto é opcional. Você deseja votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
        if pergunta == 'S':
            print('Você será encaminhado para o sistema de votação...')
            return 'sim'
        elif pergunta == 'N':
            print('Agradecemos a sua atenção.')
            return 'não'
        while pergunta != 'S' and pergunta != 'N':
          print('Não conseguimos entender sua resposta. Tente novamente:')
          pergunta = input('O seu voto é opcional. Você deseja votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
          if pergunta == 'S':
              print('Você será encaminhado para o sistema de votação...')
              return 'sim'
          elif pergunta == 'N':
              print('Agradecemos a sua atenção.')
              return 'não'
 elif ano <= 2003:
    print('Voto OBRIGATÓRIO! Você será encaminhado para\no sistema de votação...')
    return 'sim'
 elif ano > 2005:
    print('Voto NEGADO! Você não tem a idade mínima necessária para\nparticipar da eleição!')
    return 'não'
 
def votacao(autorizacao, voto):
    if autorizacao == 'sim':
        if voto == 1:
            return 'candidato1'
        elif voto == 2:
            return 'candidato2'
        elif voto == 3:
            return 'candidato3'
        elif voto == 4:
            return 'nulo'
        elif voto == 5:
            return 'branco'
    else:
        pass
def total(candidato1, candidato2, candidato3, nulo, branco):
    total = (candidato1 +  candidato2 + candidato3 + nulo + branco)
    return total
def primeirolugar(candidato1, candidato2, candidato3, nulo, branco):
    resultado_parcial = [candidato1, candidato2, candidato3]
    brancos_e_nulos = [nulo, branco]
    # separei brancos e nulos, pois pensei em colocar a condição de,
    #caso os votos brancos e nulos fossem iguais ou maiores que os outros,
    #invalidar a eleição, porém como o enunciado não pede, fica só a ideia akshakhskas
    print(f'Votos Brancos: {branco}\nVotos Nulos: {nulo}')
    vencedor = max(resultado_parcial)
    if vencedor == candidato1 and vencedor == candidato2:
        print(f'Tivemos um empate técnico entre o Jacaré e o Sapo, ambos com {vencedor} votos!')
    elif vencedor == candidato1 and vencedor == candidato3:
        print(f'Tivemos um empate técnico entre o Flamingo e o Jacaré, ambos com {vencedor} votos!')
    elif vencedor == candidato2 and vencedor == candidato3:
        print(f'Tivemos um empate técnico entre o Sapo e o Flamingo, ambos com {vencedor} votos!')
    else:    
        if vencedor == candidato1:
            print(f'O eleito foi o Jacaré, com {candidato1} votos!!')
        elif vencedor == candidato2:
            print(f'O eleito foi o Sapo, com {candidato2} votos!!')
        elif vencedor == candidato3:
            print(f'O eleito foi o Flamingo, com {candidato3} votos!!')
def segundolugar(candidato1, candidato2, candidato3):
    resultado_parcial = [candidato1, candidato2, candidato3]
    vencedor = max(resultado_parcial)
    terceirolugar = min(resultado_parcial)
    
    if candidato1 != vencedor and candidato1 != terceirolugar:
        print(f'Em segundo lugar, temos o Jacaré, com {candidato1} votos!')
    elif candidato2 != vencedor and candidato2 != terceirolugar:
        print(f'Em segundo lugar, temos o Sapo, com {candidato2} votos!')    
    elif candidato3 != vencedor and candidato3 != terceirolugar:
        print(f'Em segundo lugar, temos o Flamingo, com {candidato3} votos!')
def terceirolugar(candidato1, candidato2, candidato3):
    resultado_parcial = [candidato1, candidato2, candidato3]
    terceiro = min(resultado_parcial)
    if terceiro == candidato1 and terceiro == candidato2:
        print(f'Nas últimas duas posições, tivemos o Sapo e o Jacaré, ambos com {terceiro} votos! Empate!')
    elif terceiro == candidato1 and terceiro == candidato3:
        print(f'Nas últimas duas posições, tivemos o Jacaré e o Flamingo, ambos com {terceiro} votos! Empate!')
    elif terceiro == candidato2 and terceiro == candidato3:
        print(f'Nas últimas duas posições, tivemos o Flamingo e o Sapo, ambos com {terceiro} votos! Empate!')    
    else:
        if terceiro == candidato1:
            print(f'E em último lugar, o Jacaré, com {candidato1} votos!')
        elif terceiro == candidato2:
            print(f'E em último lugar, o Sapo, com {candidato2} votos!')
        elif terceiro == candidato3:
            print(f'Em último lugar, o Flamingo, com {candidato3} votos!')
    

import time
print('=+~-'*10)
print('      E L E I Ç Ã O  A N I M A L')
print('=+~-'*10)
apresentação = 0
print('Bem-vindo(a) ao sistema animal de eleições.\nPedimos aqui sua TOTAL SERIEDADE nos critérios de votação\noferecidos pelo sistema.')
time.sleep(1)
print('Vamos coletar dados importantes.')
print('➜  '*15)
print()
while Sistema == True:
    print('࿐༄࿔༄࿐༄'*7)
    Farofa = int(input(' ANO DE NASCIMENTO:    |'))
    print('࿐༄࿔༄࿐༄'*7)

    autorizacao = autoriza_voto(Farofa)
    if autorizacao == 'sim':
        if apresentação == 0:
            print('Uma rápida apresentação dos nossos candidatos!\n(Ela só ocorrerá no primeiro voto.)')
            time.sleep(0.6)
            print('☆ ★ '*20)
            print('   CANDIDATO 1:    JACARÉ')
            print('☆ ★ '*20)
            time.sleep(2)
            print()
            print('O Jacaré é bem influente entre os animais, e também muito temido.\nO reptiliano consegue ficar por uma hora debaixo da água, e também\num ano sem comer.\n\nTamanha popularidade o torna um bom candidato!')
            time.sleep(7)
            print()
            print()
            print('☆ ★ '*20)
            print('   CANDIDATO 2:    SAPO')
            print('☆ ★ '*20)
            time.sleep(2)
            print()
            print('O Sapo é um cara sábio e sossegado, que vive entre o mar e a terra.\nPor ser um anfíbio, conhece todo tipo de gente\ne percebe de perto as dificuldades\nde cada povo. É como um amigo pra todos!\n\nAlém da influência, é ágil e não faz vista grossa pra corrupção!\n(apesar do tamanho dos olhos)')
            time.sleep(7)
            print()
            print()
            print('☆ ★ '*20)
            print('   CANDIDATO 3:    FLAMINGO')
            print('☆ ★ '*20)
            time.sleep(2)
            print()
            print('Lindo e Poderoso. O Flamingo não é tão popular entre alguns peixes, visto que\nse alimenta deles, porém, é fato que mesmo sendo uma ave,\nele sempre está próximo à terra e ao mar, além de possuir\ntécnica e graciosidade em seus vôos.\n\nUm belo candidato, você não acha?')
            time.sleep(7)
            apresentação = 1
        else:
            pass
        print('=+~-'*13)
        print()
        Nescau = int(input('Vote! Utilize os números para escolher seu candidato!\n\n[1] - Jacaré\n[2] - Sapo\n[3] - Flamingo\n[4] - Nulo\n[5] - Branco\n'))
        Café = votacao(autorizacao, Nescau)
        if Café == 'candidato1':
            Jacaré += 1
        elif Café == 'candidato2':
            Sapo += 1
        elif Café == 'candidato3':
            Flamingo += 1
        elif Café == 'nulo':
            Nulo += 1
        elif Café == 'branco':
            Branco += 1
        pergunta = input('Voto Registrado. Mais alguém pra votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
        if pergunta == 'S':
            pass
        elif pergunta == 'N':
            Sistema = False
        else:
            while pergunta != 'S' and pergunta != 'N':
                print('Não conseguimos entender sua resposta. Tente novamente:')
                pergunta = input('Mais alguém pra votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
                if pergunta == 'S':
                   pass
                elif pergunta == 'N':
                   Sistema = False
    elif autorizacao == 'não':
        pergunta = input('Mais alguém pra votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
        if pergunta == 'S':
           pass
        elif pergunta == 'N':
           Sistema = False
        else:
            while pergunta != 'S' and pergunta != 'N':
                print('Não conseguimos entender sua resposta. Tente novamente:')
                pergunta = input('Mais alguém pra votar?\nResponda com "S" para Sim\nResponda com "N" para Não').upper()
                if pergunta == 'S':
                   pass
                elif pergunta == 'N':
                   Sistema = False

print('=+~-'*10)
print('      RESULTADO FINAL')
print('=+~-'*10)
print()
primeirolugar(Jacaré, Sapo, Flamingo, Nulo, Branco)
segundolugar(Jacaré, Sapo, Flamingo)
terceirolugar(Jacaré, Sapo, Flamingo)
votos = total(Jacaré, Sapo, Flamingo, Nulo, Branco)
print()
print(f'Total de Votos: {votos}\nAgradecemos o comparecimento de todos!')