# Passo 1: Criando um dicionário
# O dicionário 'estudante' armazena informações de um aluno.
estudante = {
    "nome": "Carla",                     # Nome do aluno
    "idade": 21,                        # Idade do aluno
    "curso": "Engenharia de Software",  # Curso que está matriculado
    "notas": [8.5, 7.0, 9.0],           # Notas obtidas nas provas
    "bolsista": True                    # Status se é bolsista ou não
}
print("Dicionário inicial:", estudante)  # Exibindo o dicionário completo

# Passo 2: Acessando valores
# Usamos as chaves para acessar os valores específicos do dicionário
print("\nNome do estudante:", estudante["nome"])  # Acessa o nome
print("Notas do estudante:", estudante["notas"])  # Acessa as notas

# Passo 3: Adicionando novos pares chave: valor
# Adicionando um novo dado sobre o estudante
estudante["projetos_concluidos"] = 3  # Número de projetos concluídos
print("\nDicionário após adicionar projetos concluídos:", estudante)

# Passo 4: Atualizando valores
# Alterando a idade do estudante
estudante["idade"] = 22  # Atualizando a idade para 22
print("\nIdade atualizada:", estudante["idade"])

# Passo 5: Removendo pares chave: valor
# Removendo o status de bolsista do dicionário
estudante.pop("bolsista")  # Remove a chave 'bolsista' e seu valor
print("\nDicionário após remover o status de bolsista:", estudante)

# Passo 6: Iterando no dicionário
# Exibindo apenas as chaves
print("\nChaves do dicionário:")
for chave in estudante.keys():
    print(chave)

# Exibindo apenas os valores
print("\nValores do dicionário:")
for valor in estudante.values():
    print(valor)

# Exibindo pares chave: valor
print("\nPares chave: valor do dicionário:")
for chave, valor in estudante.items():
    print(f"{chave}: {valor}")
    
    '''
    O que este código faz
Cria o dicionário estudante com dados variados (nome, idade, curso, etc.).
Acessa informações específicas usando as chaves.
Adiciona uma nova informação ao dicionário.
Atualiza um valor existente (idade).
Remove uma chave e seu valor (status de bolsista).
Itera pelas chaves, valores e pares chave-valor, exibindo-os.
Como rodar
Copie este código para o seu editor Python, como o VS Code.
Execute-o para ver cada etapa sendo demonstrada e explicada nos comentários.
'''