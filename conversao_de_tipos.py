# CONVERSÃO DE TIPOS

idade = '26'
numero1 = '10'
numero2 = '20'
numero3 = 30

# print(numero1 + numero2) # concatena as 2 textes (strings)
# print(numero1 + numero3) # apresenta um erro, não é possível somar uma string e um número inteiro

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# int()
# str()
# float()
# bool()

altura = float( input('Informe a sua altura '))

print(altura, type(altura))