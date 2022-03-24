frase = "O Brasil é o país do futebol, o Brasil é penta"

lista_1 = frase.split(' ')
lista_2 = frase.split(',')

for palavra in lista_1:
    print(palavra)

for trecho_frase in lista_2:
    # strip tira os espaços do começo e final string
    # capitalize deixa a primeira letra maiúscula
    print(trecho_frase.strip().capitalize())

# join junta uma lista com determinado caracter
lista_3 = '|'.join(lista_1)
print(lista_3)


for indice, valor in enumerate(lista_1):
    print(f'{indice}: {valor}')

