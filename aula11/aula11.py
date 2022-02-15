"""
Operadores lógicos
and, or, not
in e not in
"""

num1 = 12
num2 = 3

if not num1 < num2:
    print("Número não é menor")

nome = "bruninn"
if "a" not in nome:
    print("Não Existe a letra")
else:
    print("Existe a letra")

login = input("Digite o login ")
senha = input("Digite a senha ")

login_bd = "brunin"
senha_bd = "2344"

if login == login_bd and senha == senha_bd:
    print("Logado")
else:
    print("Login ou senha inválidos")

