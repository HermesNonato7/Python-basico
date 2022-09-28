# > MÉTODOS DE LISTAS

# o método é uma função que está trelada a variável

lista = [1, 3,  12, 8, 2]

# APPEND

# Adiciona um elemento no final da lista



print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# INSERT

# No insert se escolhe a posição em que quer colocar o elemento em um lista

lista.insert(2, 10)

print('Depois do insert: ', lista)

# EXTEND

# Pega os elementos de uma lista2 e coloca no final da lista

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

# POP

# Remove o elemento específico, se não especificar remove o último elemento

lista.pop()

print('Lista após o pop: ', lista)

lista.pop(0)

print('Lista após o pop: ', lista) # especificando o elemento

# REMOVE

# Você especifica qual o elementio quer remover, não remove o indice- procura o elemento e remove
# O remove sempre remove o primeiro elemento que ele encontra

lista.remove(3)

print('Depois do remove: ', lista)

# COUNT

# Ele conta a quantidade de elementos definidos que tiverem repetidos na lista

print('Quantidade de 2  na lista: ', lista.count(2))

# INDEX

# Diz o indice de um determinado elemento na lista

print('Qual é o índice do elemento 12: ', lista.index(12))

# SORT

# Esse método ordena de forma crescente a lista

lista.sort()

print(lista)

# SORT - Ordenar de forma decrescente

lista.sort(reverse=True)

print(lista)

# FUNÇÕES PARA LISTAS

# Len

print(len(lista))

# Sum

print(sum(lista))

# max

print('Maior elemento da lista: ', max(lista))

# min

print('Menor elemento da lista: ', min(lista))