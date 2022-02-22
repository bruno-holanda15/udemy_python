frase = 'O rato roeu a roupa do rei de roma'  # Iterável

tamanho_frase = len(frase)
cont = 0
nova_frase = ''
letra_maisc = input('Qual letra deseja maiuscula? ')

# Ato de percorrer cada index da str frase
while cont < tamanho_frase:
    letra = frase[cont]
    if letra == letra_maisc:
        letra = letra.upper()

    nova_frase += letra
    cont += 1

print(frase)
print(nova_frase)
