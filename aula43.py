'''
frase = 'sport'

i = 0
tam_string = len(frase)

while i < tam_string:
    print(frase[i])

    i += 1
'''
'''
senha_correta = '12345'
senha_digitada = ''
repeticoes = 0

while senha_correta != senha_digitada:
    senha_digitada = input (f'Digite sua senha:({repeticoes}x)')
    repeticoes += 1

print (repeticoes)
print ('laço acima pode ter infinita repetiçoes')
'''

texto = 'sport'
novo_texto = ''

for letra in texto: 
    print (letra)
    novo_texto += f'*{letra}'
print (novo_texto)
