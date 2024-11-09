# Exemplo 1: Comparação que retorna booleano
a = 7
b = 10

# Comparação usando '>'
maior_que = a > b  # False, pois 7 não é maior que 10
print("7 é maior que 10?", maior_que)

# Comparação usando '=='
igual = a == b  # False, pois 7 não é igual a 10
print("7 é igual a 10?", igual)

# Exemplo 2: Operadores lógicos
# Variáveis booleanas
x = True
y = False

# Usando 'and' - ambos precisam ser True para resultar em True
resultado_and = x and y
print("x and y:", resultado_and)  # False, pois y é False

# Usando 'or' - basta um ser True para resultar em True
resultado_or = x or y
print("x or y:", resultado_or)  # True, pois x é True

# Usando 'not' - inverte o valor booleano
resultado_not = not x
print("not x:", resultado_not)  # False, pois x é True e 'not' inverte para False

# Exemplo 3: Condicional com booleano
idade = 20
is_adult = idade >= 18  # Isso será True, pois 20 é maior que 18

if is_adult:
    print("Você é adulto!")  # Esse código será executado
else:
    print("Você é menor de idade.")

# Exemplo 4: Conversão para booleano
print(bool(0))         # False, pois 0 é considerado "falso" em Python
print(bool(1))         # True, pois 1 é considerado "verdadeiro" em Python
print(bool(""))        # False, pois string vazia é "falso"
print(bool("Python"))  # True, pois a string não está vazia

'''
Comparações: O código compara a e b usando >, == e mostra o resultado booleano.
Operadores Lógicos: Mostra como and, or e not funcionam para combinar e inverter valores booleanos.
Condicional: Usa if com um valor booleano (is_adult) para decidir qual mensagem exibir.
Conversão para Booleano: Usa bool() para ver quais valores são considerados True e False.
'''