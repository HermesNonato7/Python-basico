# > Variáveis

# 1. Variáveis

'''idade = 26 # cirando uma variável

print(idade)

nome =  'Hermes Nonato'

print(nome)'''

'''
Tipos de variáveis

1. int: números ionteriros, ou seja, números sem parte decimal: 0, 5, -1, 1000
2. float: números reais, ous eja, números com parte decimal: 1.0, -2,7, 3.14
3. str: cadeia de caracteres, ou seja, dados textuais
4. bool: valores lógicos, (booleanos): True ou False (sempre com a primeira letra maiúscula)
'''

'''idade = 36 # int
altura = 1.73 # float
nome = 'Hermes Nonato' # str654
estudando = True # booleano (bool)'''

# Use o comando type para saber o tipo da variável

'''print( type(idade) )
print( type(altura) )
print( type(nome) )
print( type(estudando) )'''

# obtendo dados do usuário e salvando em uma variável

''' linguagem = input('Qual é a linguagem de programação que você está estudando? ')

print( 'A linguagem que vocês está estudando é: ', linguagem) '''

# Exercício: imprima vários tipos de variáveis 

nome = input('Digite o seu nome: ') + '!'
idade = input('Digite a sua idade: ')
altura = input('Digite sua altura: ')
estudando = input('Você está estudando? Digite True para sim ou False para não: ')
linguagem = input('Qual linguagem de programação você está estudando? ') 

print('\n Seja bem vindo ' , nome , '\n Sua idade é: ',str(idade), '\n Sua altura é: ',str(altura),
 '\n Você está estudando: ',str(estudando), '\n A linguagem que você está estudando é: ',linguagem)

'''print('Sua idade é: '  +  str(idade))
print('Sua altura é: ' + str(altura))
print('Você está estudando: ' + str(estudando)) 
print('A linguagem que você está estudando é: ' + linguagem)'''