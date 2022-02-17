"""
Condições IF, ELIF, E ELSE
"""

if False:
    print("True")
else:
    print("False")
    num_1 = 3
    num_2 = 4
    print(num_1 + num_2)

senha = input("Digite sua senha ")

# várias condições, tomar cuidado com a utilização (CLEAN CODE)
if senha == "1234":
    print("Senha muito simples")
elif senha == "mudarsenha":
    print("Precisa mudar a senha")
else:
    print("Não achamos sua senha")


