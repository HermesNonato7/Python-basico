# > ESTRUTURAS CONSICIONAIS

# IF, ELSE e ELIF

''' idade = 18

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')'''

'''
Imagine que você queira imprimir "Aprovada(o)", caso o estudante tenha uma média
superior ou igual  a 7, e "Reprovado", caso a média seja inferior a 7.
'''

'''media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi aprovada(o)!')
elif media >= 5:
    print("Recuperação")
else:
    print('Você foi reprovada(o)')'''

media = 10
presenca = 60

if media >= 7 and presenca >= 70:
    print('Aprovada(o)!')
    print('Parabéns!')
else:
    print('Reprovada(a)')
    print('Tente novamente.')
