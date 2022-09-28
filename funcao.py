# > FUNÇÕES

# 1. O que são funções e porque utiliza-las?

# Funções que utilizamos anteriormente...

'''print() # Imprime uma mensagem (int, float, str) no console (terminal, cmd)
input() # Retorna um dado informado pelo usuário (entrada padrão) e pode ser uma string...
len() # Recebe uma lista e retorna  o tamanho  dessa lista
max() # retorna o maior valor de uma lista

# A função deve-se criar e chama-la pelo nome, senão ela não é iniciada'''

# 2.  Criação de funções 

# Uma função inicial
# DEF vem de define (definindo uma função)

'''def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()'''

# Função com parâmetro

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Hermes', 'Python')
saudacao('Lucas', 'JavaScript')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Hermes')
# saudacao('Hermes', 'C++')

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)

# Como reaproveitar as funções- Exemplo

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20)
# resultado = calculadora(10, 20, '-')

print(resultado)

 
