'''
O método get() é usado para acessar o valor de uma chave de maneira segura. Se a chave não existir, ele retorna None (ou um valor padrão que você definir), sem causar erro.
'''
# Criando um dicionário com informações de um estudante
estudante = {"nome": "Ana", "idade": 20, "curso": "Matemática"}

# Acessando o valor da chave "nome" usando get()
print(estudante.get("nome"))  # Saída: Ana

# Tentando acessar uma chave inexistente usando get()
print(estudante.get("bolsista"))  # Saída: None

# Usando get() com valor padrão
print(estudante.get("bolsista", "Não informado"))  # Saída: Não informado

'''
Por que usar get()?

Ele evita erros ao acessar chaves inexistentes.
Permite definir um valor padrão para retorno.
'''