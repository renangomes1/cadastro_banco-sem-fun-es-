
Nome = input('Digite seu nome>>')
CPF = input('Digite seu CPF>>')
Senha = input('Digite sua senha>>')
print(f'Olá {Nome}, Seja bem vindo(a)!')

print('Escolha uma das opções abaixo:')
print('OBS: Escolha um número para uma da opções desejadas')


saldo = 0

while True:
    print('BANCO')
    print('1. Ver extrato')
    print("2. Fazer um depósito")
    print("3. Fazer um saque")
    print("4. Sair do sistema")
    

    opção = input('Escolha uma opção')


    if opção =='1':
      print(f"Saldo atual: R${saldo:.2f}")
    elif opção == '2':
        valor = float(input('Digite o valor do depósito'))
        if valor>0:
         saldo += valor
         print(f'Deposito de {saldo:.2f} feito com sucesso')
        else:
         print('o valor deve ser positivo')
    elif opção == '3':
    
            valor = float(input('Digite o valor do saque: R$'))
            if valor > 0:
                if valor <= saldo:
                 saldo -= valor
                 print(f' Saque de {saldo:.2f} feito com sucesso')
                else:
                 print('Saldo insuficiente')
            else:
             print('o valor deve ser positivo')
    elif opção == '4':
       print('Saindo do sistema... ')
       break
    



