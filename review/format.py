a = 'AAA'
b = 'BBBBBB'
c = 1.1
d = True

string = 'a={}, b={seg_parametro}, c={ter_parametro:.3f}'
# Após adicionar parâmetro nomeado, os próximos
# precisam ser nomeados também
formato = string.format(
    a, seg_parametro=b, ter_parametro=c
)

print(formato)
