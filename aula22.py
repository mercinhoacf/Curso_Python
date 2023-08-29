entrada = input ('{E}ntrar ou {S}air')
senha_digitada = input ('Senha:')

if entrada == 'E' or entrada == 'e' and senha_digitada == '1234':
    print ('Você entrou!:)')
elif entrada == 'E' or entrada == 'e' and senha_digitada != '1234':
    print ('Você digitou a senha incorreta!')
else: 
    print ('Você saiu!')   
