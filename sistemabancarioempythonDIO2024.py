saldo_total = 0
limite_de_saque = 500
extrato = ""
numero_de_saques_feitos = 0
limite_de_vezes_de_saque_por_dia = 3
valor = 0
 
while True:
    menu = ('''\n=======Menu=======
       
    Escolha uma opção:

    [1] Sacar.
    [2] Depositar.
    [3] Extrato.
    [4] Sair do sistema.
       
 ===================\n''')
    opção = input(menu)
     
    if opção == "1":
        if saldo_total == 0:
            print("\nNão é possível fazer saque porque não há saldo.\n")
        elif numero_de_saques_feitos >= limite_de_vezes_de_saque_por_dia:
            print("\nLimite diário de saques atingido.\n")
        else:
            valor = float(input("\nEscolha uma quantia para sacar:\n"))
            if valor > saldo_total:
                print("\nOperação não concluída. Saldo insuficiente.\n")
            elif valor <= 500 and valor <= saldo_total:
                saldo_total -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques_feitos += 1
            else:
                 print("\nValores acima de 500 reais não são permitidos para saque.\n")
    
    elif opção == "2":
        valor = float(input("\nEscolha uma quantia para depositar:\n"))
        if valor <= 0:
            print("\nOperação não concluída. Escolha uma quantia válida para depositar.\n")
        else:
            saldo_total += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opção == "3":
        print("\n=======Extrato=======\n")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo_total:.2f}")
        print("\n=====================\n")

    elif opção == "4":
        break
 
    else:
        print("\nEscolha uma opção válida do menu.\n")
