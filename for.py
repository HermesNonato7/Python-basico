# LAÇOS DE REPETIÇÃO: FOR | AULA 08

# Explorando melhor a  função range

''' for variavel in range(10): # Esse paramero vai de 0 até o limite dado menos 1 (-1)
    print(variavel) '''

''' for variavel in range(1, 11): # assim vai de 1 até 10
    print(variavel) '''

# 1, 4, 7, 10
''' for variavel in range(1, 12, 3): # 3 valores: início, parada e passo(step)
    print(variavel)  '''

# Aplicação prática do FOR

'''nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
nota3 = float(input('Informe sua nota 3: '))'''

# Aplicação prática do FOR
# Estrutura automatizada para obtenção das 3 notas

soma= 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota

print(soma / 3)