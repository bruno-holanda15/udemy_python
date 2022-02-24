secreta = 'perfume'

fim_de_jogo = True
lista_letras_certas = []
tentativas = 5

while fim_de_jogo:

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Só pode digitar uma letra')
        continue

    if letra in secreta:
        lista_letras_certas.append(letra)
        print('Acertou')
    else:
        tentativas -= 1
        if tentativas <= 0:
            print('Você perdeu o jogo!')
            break

        print(f'Errou, cuidado, só tem mais {tentativas}')

    palavra_temp = ''
    for le in secreta:
        if le in lista_letras_certas:
            palavra_temp += le
        else:
            palavra_temp += '*'

    print(palavra_temp)

    if palavra_temp == secreta:
        print('Parabéns!')
        break


