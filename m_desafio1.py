## Desafio DIO CRIANDO UM SISTEMA BANCÁRIO
## Operações SACAR, DEPOSITAR, EXTRATO

## DEPÓSITO 
## Apenas valores positivos 
## Armazemar histório em uma variável e exibidos na operação extrato

## SAQUE
## Apenas valores positivos
## Limite de 3 saques diários
## Limite de 500 reais por saque
## Caso não possuo saldo em conta o sistema deve informar o usuário
## Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato

## EXTRATO 
## Todos os depósitos e saques devem estar listados
## No final deve mostra o saldo atual da conta
## Caso o extrato estiver em branco exibir uma mensagem: Não foram realizadas movimentações 
## Usar o formato R$ 1500.00

menu = """
          
***********************************************************************************
Bem vindo ao NOSSO BANCO
Escolha a opção desejada:

[C] - Consulta Saldo         
[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair

***********************************************************************************
--> """

saldo_conta = 0
extrato = ""
valor_limite_saque = 500
quantidade_saque = 0
limite_quantidade_saque = 3

while 1 == 1:
    escolha = input (menu)
    escolha = escolha.upper()

    if escolha == "D":
        valor = float(input("Por favor informe o valor do depósito: "))
        if valor > 0:
            saldo_conta += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação não realizada, valor inválido, tente novamente.")
    elif escolha == "S":
        valor = float(input("Informe o valor do saque: "))

        maior_que_saldo = valor > saldo_conta
        maior_que_limite = valor > valor_limite_saque
        maior_que_quantidade_saques = quantidade_saque >= limite_quantidade_saque
        if maior_que_saldo:
            print("Operação não realizada, saldo insulficiente.")    
        
        elif maior_que_quantidade_saques:
            print("Operação não realizada, quantidade de saques excedido.")

        elif maior_que_limite:
            print("Operação não realizada, valor excede o limite por operação.")

        elif valor > 0:
            saldo_conta -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saque += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação não realizada, valor inválido, tente novamente.")

    elif escolha =="E":
        print("\n******************************* EXTRATO NOSSO BANCO *******************************")
        print("NÃO HÁ HISTÓRICO DE OPERAÇÕES REALIZADAS." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("\nObrigado por utilizar nossos serviços.")
        print("\n***********************************************************************************")

    elif escolha =="C":
        print("\n******************************* SALDO NOSSO BANCO *********************************")
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("\nObrigado por utilizar nossos serviços.")
        print("\n***********************************************************************************")

    elif escolha == "Q":
        break

    else:
        print("Opção inválida, tente novamente")        

        
    
