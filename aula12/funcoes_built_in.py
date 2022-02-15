num1 = input('Digite um número : ')
num2 = input('Digite outro número : ')

# isnumeric isdigit isdecimal , se tiver ponto ele retorna false
if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num2 + num1)
else:
    print("Não pude converter")

#Maneira de executar com floats
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num2 + num1)
except:
    print('ERROR')
