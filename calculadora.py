
while True:
    operacao= input("escolha qual vai ser operação + - / *:  ")

    if operacao != '+' and operacao != '-' and operacao != '/' and operacao != '*':
        print('Digite a operação correta')
        continue

    num_1 = int(input("Digite um numero: "))
    num_2 = int(input("Digite outro numero: "))

    if operacao == '+':
        resultado =  num_1 + num_2
        print(f'{num_1} + {num_2} = {resultado}')

    if operacao == '-':
        resultado = num_1 - num_2
        print(f'{num_1} - {num_2} = {resultado} ')