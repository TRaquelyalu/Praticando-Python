''' 
As listas são coleções de itens mutáveis (você pode alterar, adicionar ou remover elementos) e permitem itens duplicados.

Características das listas:
Definidas com colchetes [].
Podem conter diferentes tipos de dados (números, strings, listas aninhadas, etc.).
A ordem dos elementos é mantida.
'''
#Exemplo: Criando uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

#Acessando elementos de uma lista
#Os índices começam do 0.
print(frutas[0])  # Primeiro item: maçã
print(frutas[-1]) # Último item: laranj


#Alterando elementos
frutas[1] = "uva"  # Substitui "banana" por "uva"
print(frutas)

'''
Adicionando e removendo elementos
append(): Adiciona um item ao final.
insert(): Adiciona um item em uma posição específica.
remove(): Remove um item específico.
pop(): Remove pelo índice (ou o último por padrão).
'''

frutas.append("abacaxi")  # Adiciona no final
frutas.insert(1, "morango")  # Adiciona "morango" na posição 1
frutas.remove("uva")  # Remove "uva"
frutas.pop()  # Remove o último item (abacaxi)
print(frutas)

#Iterando em listas
for fruta in frutas:
    print(fruta)