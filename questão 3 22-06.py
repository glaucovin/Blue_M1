nome = input('Bem-vindo ao sistema de notas da escola. Digite o seu nome:')
media = float(input('Digite sua nota: "Digite ponto ao invés da vírgula"').replace(",", "."))
dicionario = {nome: media}
if media >= 7:
    print(f'{nome} está aprovado(a)!')
elif media <= 6.9 and media >= 5:
    print(f'{nome} está de recuperação!! Estude mais!')
else:
    print(f'{nome} está reprovado!')

print(dicionario)