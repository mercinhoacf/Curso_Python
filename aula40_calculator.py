while True:
    num1 = input ('Digite um número: ')
    num2 = input ('Digite um número: ')
    operador = input ('Digite um opearador: ')
    num_validos = None
    # num1_float = 0
    # num2_float = 0
    # soma = float (num1 + num2)
    # sub = float (num1 - num2)
    # multi = float (num1 * num2)
    # div = float (num1 / num2)

    try:
        num1_float = float (num1)
        num2_float = float (num2)
        num_validos = True

    except: 
        num_validos = None

    if num_validos is None: 
        print ('numeros digitados sao invalidos.')
        continue 

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('Operador invalido')
        continue 

    if len(operador) > 1:
        print ('Digite apenas um operador')
        continue


    print ('Fazendo sua conta!')
    if operador == '+':
        print (f'{num1_float}+{num2_float}=',num1_float + num2_float )
    elif operador == '-':
        print (f'{num1_float}-{num2_float}=',num1_float - num2_float)
    elif operador == '*':
        print (f'{num1_float}*{num2_float}=',num1_float * num2_float)
    elif operador == '/':
        print (f'{num1_float}/{num2_float}=',num1_float / num2_float)
    else:
        print ('Você fez algo errado!')
    
    
        

    sair = input ('Quer sair? [s]im: ')
    sair = sair.lower().startswith('s')

    if sair is True:
        break
