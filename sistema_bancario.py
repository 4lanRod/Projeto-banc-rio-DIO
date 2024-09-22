menu = ("Digite a opção que deseja executar:\n [d] depositar\n [s] Sacar\n [e] Extrato \n [q] Sair\n\n " )
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input(menu))
    if opcao == "d":    
        valor = float(input("Digite o valor que deseja depositar "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

    elif opcao == "s":

        valor = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! saldo insuficiente ")
        
        elif excedeu_limite:
            print("Você utrapassou o limite disponivel ")
        
        elif excedeu_saque:
            print("você execedeu o numero de saques disponivel no dia, volte após 24 horas")
 
        

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falhou o valor informado é inválido")

    elif opcao == "e":

        print("\n=============EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: no valor de  R$ {saldo:.2f}")
        print("==================================")

    elif opcao == "q":
        break
    else:
        print("Operação invalida, digite novamente a opção desejada.")