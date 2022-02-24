"""
list - pode conter vários tipos de dados
functions - append, insert, pop, del, clear, extend...
min, max
range
"""

# index   0      1        2    3     4
lista = ['A', 'Banana', True, 234, 232.43]
# index - 4      3        2    1    0

# podemos fatiar listas tbm
# print(lista, lista[2], lista[0:3], lista[2:], lista[:4])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# l2.append('blzinha') # adiciona como último valor o blzinha
# l1.insert(2, 'banana') adiciona no index 2 o value banana

l3 = l1 + l2
l1.extend(l2) # concatena no final da lista outra lista
l3.pop() # remove o último elemento

# print(l1, l3)


l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# del(l4[2:4]) # deleta os valores da lista ou item da lista
# del(l4[0])
# print(max(l4), min(l4))

l2 = list(range(1,12)) # com a função built in list ela transforma a range dentro dela em uma list, como se fosse um type cast
# print(l2)