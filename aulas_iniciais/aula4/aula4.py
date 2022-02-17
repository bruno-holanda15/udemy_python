"""
Tipos de dados primitivos
str - string - textos 'Assim "assim"
int - inteiro - 12234 0 -12 -23232
float - número real com casas decimais - +230.012 -32333.233
bool - boolean - true  false - (10 == 10 -- true)
"""

print("Bruno", type("Bruno"))
print(12, type(12))
print(12.2, type(12.2))
print(10 == 10, type(10 == 10))
print(27 < 18, type(27 < 18))

# trocando tipo
print('10', type('10'), type(int('10')))
print('10.12', type('10.12'), type(float('10.12')))

# algumas conversões não são executadas por ValueError como essa abaixo
# print('10.12', type('10.12'), type(int('10.12')))

