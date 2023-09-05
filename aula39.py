# nome = 'Emerson Aquino'
# size_nome = len(nome)
# print (nome)
# print (size_nome)

nome = 'Emerson Aquino'

indice = 0
new_name = ''
while indice < len(nome):
    letra = nome [indice]
    new_name += f'*{letra}'
    indice += 1

new_name += '*'
print (new_name)
