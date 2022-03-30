idade = int(input('Digite sua idade: '))

def verifica_maioridade(idade):
    return True if idade > 18 else False

while not verifica_maioridade(idade):
    idade = int(input('Digite sua idade: '))

print('Finalmente')

