# Definindo a variável idade com o valor 10
idade = 10

# Verificando se a idade é maior ou igual a 18
if idade >= 18:
    # Se a condição for verdadeira, imprime que a pessoa é maior de idade
    print("Você é maior de idade")

# Verificando se a idade é maior ou igual a 13 (se a primeira condição for falsa)
elif idade >= 13:
    # Se a condição for verdadeira, imprime que a pessoa é um adolescente
    print("Você é um adolescente")

# Se nenhuma das condições anteriores for verdadeira (no caso, idade < 13)
else:
    # Imprime que a pessoa é uma criança
    print("Você é uma criança")