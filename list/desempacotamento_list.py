"""
Desempacotamento de listas
"""

lista = ['João', 'Luiz', 'Carla', 1, 2, 3, 4, 5, 7, 8, 9, 10]

# asterisco completa os itens para a variável
n1, n2, *outra_lista, n3, n4 = lista

print(n1, n2, outra_lista, n3, n4)


