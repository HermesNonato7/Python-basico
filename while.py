numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

'''if numero_sorteado == numero_escolhido:
    print('Você acertou!')
else:
    print('Você errou!')''' # código limitado que não atende o proposto

while numero_escolhido != numero_sorteado:
    print('Você errou, tente novamente...')
    contador = numero_escolhido
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))
print('Parabéns! Você acertou!')

# ESTRUTURA DE CONTROLE DE FLUXO- Exemplo 2

# Criar uma estrutura com uma variavel contadora

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1

