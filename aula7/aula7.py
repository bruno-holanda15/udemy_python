import datetime

data = datetime.date.today()
ano_atual = data.year

nome = "Bruno"
altura = 1.87
peso = 84.1
idade = 26
ano_de_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura:.1f} e pesa {peso}kg.')

print(f'O IMC do {nome} é {imc:.2f}.')

print(f'{nome} nasceu em {ano_de_nascimento}.')






