"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
lembrar que todos os tipos de dados no python são class, até as functions
segundo prof, pq o python é uma linguagem muito focada para o OO
"""

"""
= é o operador de atribuição, o valor Bruno tem uma referência de memória 
no arquivo pela variável nome
"""

nome = "Brunin Top"  # str
idade = 26  # int
altura = 1.87  # float
peso = 84  # int
e_maior_de_idade = idade > 18  # bool
imc = peso / (altura ** 2)

print("Nome: " + nome, type(nome))

# utilizando f strings para formatar exibição de msg
print(f"Idade: {idade}", type(idade))

print(f"Altura: {altura}", type(altura))
print(f"É maior de idade {e_maior_de_idade}", type(e_maior_de_idade))

# float com duas casas decimais
print(f"Meu IMC é de {imc:.2f}")

# usando function format
print("{} tem {} anos e {:.1f} de imc".format(nome, idade, imc))

print("{0} tem {1} anos e {2:.1f} de imc, {0} é o ganhas".format(nome, idade, imc))





