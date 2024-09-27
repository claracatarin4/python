resp = input('deseja informar um valor para o cálculo da soma (s - sim ou n - não)?')
while resp == 's' or resp == 'S':
    num = int (input('digite um número:'))
    num2 = int(input('digite um número:'))
    soma = num + num2
    print(f'a soma de {num} + {num2} = {soma}')
    resp = input('deseja informar um valor para continuar (s - sim ou n - não)?')
print('cabou')
