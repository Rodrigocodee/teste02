def adicionar(x, y):
   return x + y

def subtrair (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y 

def divisao (x, y):
    if y != 0:
        return x / y
    else:
        print('errada! divisão por 0')

def calculadora ():
    print('selecione a operação: ')
    print('1 - adição')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')

    escolha = input('Digite a opção (1/2/3/4): ')

    if escolha in ['1','2','3','4']:
        num_1 = float(input('Digite um numero: '))
        num_2 = float(input('Digite outro numero: '))

        if escolha == '1':
            print(f'{num_1} + {num_2} = {adicionar(num_1,num_2)}')
        
        elif escolha == '2':
            print(f'{num_1} - {num_2} = {subtrair(num_1, num_2)}')

        elif escolha == '3':
            print(f'{num_1} * {num_2} = {multiplicacao(num_1,num_2)}')
        
        elif escolha == '4':
            print(f'{num_1} / {num_2} = {divisao(num_1,num_2)}')

        else:
            print('Opção invalida!')

calculadora()

