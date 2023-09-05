"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input ('Digite um número!')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_text = 'impar'

    if par_impar:
        par_impar_text = 'par'

    print (f'O numero {numero_int} é {par_impar_text}')

else: 
    print ('Voce nao digitou um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
nome = input ('Informe seu nome:')
horas = input ('Informe que horas são:')
horas_float = float(horas)

if horas_float <= 11.59 :
    print (f'Bom dia, {nome}!')

elif horas_float > 11.59 >= 17.59 :
    print (f'Boa tarde, {nome}!')

else: 
    print (f'Boa noite, {nome}!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
size_nome = len(nome)

if size_nome > 1:
    if size_nome<= 4:
        print('Seu nome é curto')
    elif size_nome >= 5 and size_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
