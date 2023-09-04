"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

print ('vou dobrar o numero que voce digitar!')
numero = input ('Digite um numero: ')
#numero_int = int(numero)

try: 
    numero_int = int(numero)
    print (f'o numero que voce digitou é {numero} e o dobro dele é {numero_int * 2}')
except: 
     print ('Isso não é um número!')

#if numero.isdigit():#mostra se o usuario digitou somente numeros
    #numero_int = int(numero)
    #print (f'o numero que voce digitou é {numero} e o dobro dele é {numero_int * 2}')

#else: 
    #print ('Isso não é um número!')

