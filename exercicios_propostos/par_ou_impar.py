def is_par(numero):
    resto_divisao = numero % 2
    if resto_divisao == 0 and numero != 0:
        return True
    else:
        return False


numero = input('Digite um número: ')

if numero.isnumeric():

    numero = int(numero)

    if is_par(numero):
        print('Número é par')
    elif numero == 0:
        print('Número é nulo')
    else:
        print('Número é impar')

else:
    print('Digite um número pf')





