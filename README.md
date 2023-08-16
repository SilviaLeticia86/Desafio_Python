# Sistema Bancário Simples

Este é um programa simples de sistema bancário que permite realizar operações de criar usuário, criar conta, depósito, saque, extrato e sair. O saldo inicial é R$200 e o limite de saque é R$500.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- [x] Criar Usuário
- [x] Criar Conta
- [x] Depositar
- [x] Sacar
- [x] Extrato
- [x] Sair

## Como usar

1. Execute o programa.
2. Escolha a opção correspondente à ação que deseja realizar.
3. Siga as instruções fornecidas pelo programa.
4. Ao selecionar a opção "Extrato", o programa exibirá uma lista de movimentos realizados e o saldo atual.

## Limitações

- O número de saques é limitado a 3.
- O limite total de saque é de R$500, incluindo o saldo disponível.

## Estrutura do Código

O código está organizado da seguinte forma:

- A classe `Usuario` representa um usuário do banco, contendo nome, data de nascimento, CPF e endereço.
- A classe `Conta` representa uma conta bancária, com agência, número da conta, usuário associado, saldo, extrato e limite de saques.
- O menu principal oferece opções para criar usuário, criar conta, depositar, sacar, extrato e sair.

## Como encerrar

Para encerrar o programa, selecione a opção "Sair".

---

**Nota:** Este é um projeto de exemplo para fins educativos e de demonstração. Não é recomendado para uso em ambiente de produção.

