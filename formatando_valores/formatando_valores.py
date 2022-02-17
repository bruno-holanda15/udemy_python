"""
Formatando valores com modificadores
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# :.(NÚMERO)f - qtd casas decimais
print(f'{divisao:.2f}')

"""
:(CARACTER)(> ou < ou ^)(QUANTIDADE)(TIP0 - str, int ou float)
> - Esquerda
< - Direita
^ - Centro
"""
nome = "Brunin Top"
num_3 = 12309
num_4 = 23.32
print(f'{num_3:#>20}')
print(f'{nome:0^20}')
print(f'{num_4:@<20}')

print(nome.ljust(18, 'L'))
print(nome.rjust(18, 'R'))
print(nome.lower())
print(nome.upper())
print(nome.title())

