# > LISTAS- Aula 09

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
# Uma lista do Python permite varios tipos juntos(dentro), pode ser craidos com float junto com int, etc.

notas = [7.9, 9.7, 8.2]

# Criando listas

lista = [] # lista vazia- listas vazia podem ser preenchidas depois
lista = list() # também cria uma lista vazia
lista = [36, 'Hermes', 3.14159, True]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [36, 'Hermes', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4]) da erro

print(lista[-1]) # o -1 é o último elemento
print(lista[-2]) # o -2 é o anti-último elemento
print(lista[-3]) # o -3 é o anti-penúltimo elemento...
print(lista[-4]) # o -4 sucessivamente ...

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista [0:3])
print(lista [3:6])
print(lista [3:])
print(lista [0:])
print(lista [2:6:2])

# > Interações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)


# 2. Utilizando os índices

print('Comprimento da lista: ', len(lista)) # len de length= comprimento

for i in range(len(lista)):
    # print(i)
    print(lista[i]) # imprime cada item da lista pelo i
