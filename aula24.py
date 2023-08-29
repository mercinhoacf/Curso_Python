# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  E m e r s o n
# -7-6-5-4-3-2-1
nome = 'Emerson'
print (nome[2])
print (nome[3])
print (10 * '-')
print ('r' in nome)
print ('r' not in nome)

nome = input ('digite seu nome:')
encontrar = input ('o que voce deseja encontrar')

if encontrar in nome:
    print (f'{encontrar} está {nome}')
else: 
    print (f'{encontrar} não está em {nome}')
