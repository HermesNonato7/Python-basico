# > DICIONÁRIOS

# Criando dicionários

dicionario = {} # definindo um dicionário vazio
dicionario = dict() # outra forma de criar um dicionário vazio

dicionario = { 'nome' : 'Hermes', 'idade' : 36, 'altura' : 1.73 }

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2 # se a chave já existe ela subscreve

print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)