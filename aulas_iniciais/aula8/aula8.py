"""
Entrada de dados - usando function input
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

# type cast int() - transformando o str em int
ano_nascimento = 2021 - int(idade)


print(f'{nome} tem {idade} anos. {nome} nasceu no ano de {ano_nascimento}')

numero_1 = int(input("Digite um número "))
numero_2 = input("Digite outro número ")
numero_2 = int(numero_2)

print(numero_1 + numero_2)
