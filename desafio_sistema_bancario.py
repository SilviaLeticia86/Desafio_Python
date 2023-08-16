menu = """

[c] Criar Usuário
[a] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
contas = []
proxima_conta = 1

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 200
        self.extrato = []
        self.numero_saques = 3

LIMITE_SAQUES = 3
limite = 500

def criar_usuario():
    nome = input('Digite o nome do usuário: ')
    data_nascimento = input('Digite a data de nascimento do usuário: ')
    cpf = input('Digite o CPF do usuário: ')
    endereco = input('Digite o endereço do usuário (logradouro, número, bairro, cidade, estado): ')
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print('Usuário criado com sucesso.')

def criar_conta():
    global proxima_conta
    cpf_usuario = input('Digite o CPF do usuário para vincular à conta: ')
    for usuario in usuarios:
        if usuario.cpf == cpf_usuario:
            nova_conta = Conta('0001', proxima_conta, usuario)
            contas.append(nova_conta)
            
            proxima_conta += 1
            print('Conta criada com sucesso.')
            return
    print('Usuário não encontrado.')

def saque(*, nome):
    for conta in contas:
        if conta.usuario.nome == nome:
            if conta.numero_saques < LIMITE_SAQUES:
                valor_saque = int(input('Digite o valor do saque: '))
                if valor_saque > (conta.saldo + limite):
                    print('Saldo insuficiente.')
                else:
                    conta.saldo -= valor_saque
                    conta.extrato.append(f'Saque: -R${valor_saque:.2f}')
                    conta.numero_saques += 1
                    print('Valor sacado com sucesso.')
            else:
                print('Limite de saque excedido.')
            return
    print('Conta não encontrada.')

def deposito(valor_deposito):
    saldo_conta = contas[0].saldo  
    saldo_conta += valor_deposito
    contas[0].saldo = saldo_conta
    contas[0].extrato.append(f'Depósito: +R${valor_deposito:.2f}')
    print('Depósito realizado com sucesso.')

def extrato(*, nome, posicional=False):
    for conta in contas:
        if conta.usuario.nome == nome:
            print('Extrato:')
            for movimento in conta.extrato:
                print(movimento)
            print(f'Saldo atual: R${conta.saldo:.2f}')
            return
    print('Conta não encontrada.')

while True:
    opcao = input(menu)
    
    if opcao == 'c':
        criar_usuario()
        
    elif opcao == 'a':
        criar_conta()

    elif opcao == 'd':
        valor_deposito = int(input('Digite o valor a ser depositado: '))
        deposito(valor_deposito)

    elif opcao == 's':
        nome_usuario_saque = input('Digite o nome do usuário para saque: ')
        saque(nome=nome_usuario_saque)

    elif opcao == 'e':
        nome_usuario_extrato = input('Digite o nome do usuário para extrato: ')
        extrato(nome=nome_usuario_extrato)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida. Por favor, solicite novamente a opção desejada!')
