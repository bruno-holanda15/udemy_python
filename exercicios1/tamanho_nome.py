nome = input("Digite seu nome: ")

qtd_letras = len(nome)

if qtd_letras > 6:
    print('Seu nome é muito grande')
elif qtd_letras <= 4:
    print('Seu nome é curto')
else:
    print('Seu nome é normal')

