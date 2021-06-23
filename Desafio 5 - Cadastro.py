dados = []
numero_pessoas = 0
continuacao = True
feminino = 'F'
masculino = 'M'
dicionario = {}
mulheres = []
idadesLista = []
acimaMédia = []

while continuacao == True:
    
    nome = input('Vamos guardar alguns dados.\nDigite o nome de uma pessoa\npara cadastrá-la.')
    idade = int(input('Digite a idade dessa pessoa:'))
    gen = input('Agora digite o gênero de nascença dessa pessoa. Use "F" ou "M"').upper()
    
    while gen != masculino and gen != feminino:
            gen = input('Não conseguimos computar um gênero válido. Tente novamente.').upper()
    
    idadesLista.append(idade)
    dicionario = {'Nome': nome, 'Idade': idade, 'Gênero': gen}

    if gen == feminino:
        mulheres.append(dicionario) 

    numero_pessoas += 1
    dados.append(dicionario)
    confirmacao = input('Você deseja cadastrar mais alguma pessoa?\nUse "S" para Sim\nUse "N" para não').upper()
    if confirmacao == 'N':
        continuacao = False
    elif confirmacao == 'S':
        pass
    else:
        while confirmacao != 'N' and confirmacao != 'S':
            confirmacao = input('Não conseguimos computar sua resposta. Digite novamente:\nDeseja cadastrar mais pessoas?\nUse "S" para Sim\nUse "N" para não').upper()
    
    
soma = sum(idadesLista)
mediaidade = (soma / numero_pessoas)

for i in idadesLista:
    if i > mediaidade:
        acimaMédia.append(i)
    
print(dados)
print()
print(f'O número de pessoas cadatradas foi: {numero_pessoas}')
print()
print(f'A média de idade das pessoas cadastradas é: {mediaidade}')
print()
print(f'Esses são os registros de mulheres que foram cadastradas:\n{mulheres}')
print()
print(f'As idades que estão acima da média são:\n {acimaMédia}')




