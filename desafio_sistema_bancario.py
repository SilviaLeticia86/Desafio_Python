menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 200
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        deposito = int(input('Digite o valor a ser depositado: '))
        saldo += deposito
        extrato.append(f'Depósito: +R${deposito: .2f}')
        print('Depósito realizado com sucesso.')
        
    elif opcao =='s':
        if numero_saques < LIMITE_SAQUES+4:
            valor_saque = int(input('Digite o valor do saque: '))    
            if valor_saque > (saldo + limite):
                print('Saldo insuficiente.')
            else:
                saldo -= valor_saque
                extrato.append(f'Saque: -R${valor_saque: .2f}')
                numero_saques +=1
                print('Valor sacado com sucesso.')
        else:
            print('Limite de saque excedido.')                
          
    elif opcao =='e':    
          print('Extrato:')   
          for movimento in extrato:
              print(movimento)
          print(f'Saldo atual: R${saldo: .2f}')   
     
    elif opcao == 'q':
        break      
    
    else:
        print('Operação inválida. Por favor, solicite novamente a opção desejada!')            