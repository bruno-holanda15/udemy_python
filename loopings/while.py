"""
while - looping para realizar um trecho de código
enquanto uma condição for True

comandos
    continue - pula o laço(while)
    break - encerra o laço(while)
"""
cont = 0
while cont < 100:
    if cont == 3 or cont == 7:
        cont += 1
        continue

    if cont == 13:
        break

    print(f'Contador - {cont}')
    cont += 1


