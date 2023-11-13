condicao = 10 == 10
variavel = 'Ta certo' if condicao else 'Ta errado'
print(variavel)
digito = 8 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)


# print('Valor' if False else 'Outro valor' if False else 'Fim')
