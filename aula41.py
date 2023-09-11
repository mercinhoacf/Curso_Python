string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == 'x':
        break

    print (letra)
    i += 1 

else: 
    print ('Nao encontrei na string!')

print ('Fora do while')
