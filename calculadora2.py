operacao = ' '
while operacao: 
    print('calculadora')
    print('soma: +')
    print('subtração: -')
    print('multiplicação: *')
    print('divisão: /')
    print("sair: 's' ou 'S'")
    operacao = input('insira a operacao:') 

    if operacao == "+":
        num1 = int(input('insira o primeiro valor:'))
        num2 = int(input('insira o segundo valor:'))
        soma = num1 + num2
        print(f'o resultado é {soma}')
    elif operacao == "-":
        num1 = int(input('insira o primeiro valor'))
        num2 = int(input('insira o segundo valor'))
        subtracao = num1 - num2 
        print(f'o resultado da subtração é:{subtracao}')
    elif operacao == "*":
        num1 = int(input('insira o primeiro valor'))
        num2 = int(input('insira o segundo valor'))
        multiplicacao = num1 * num2
        print(f'o resultado da multiplicação é: {multiplicacao}')
    elif operacao == "/":
        num1 = int(input('insira o primeiro valor'))
        num2 = int(input('insira o segundo valor'))
        divisao = num1 / num2
        print(f'o resultado da divisão é:{divisao}')
    if operacao == 's' or operacao == 'S':
        print("tchau")
        break