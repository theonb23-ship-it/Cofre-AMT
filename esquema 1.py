#DEFINIÇÃO DA QUANTIDADE DE DINHEIRO E VALOR INVIDUAL E TOTAL
n1 = n2 = n5 = n10 = n20 = n50 = n100 = 2
notas = (1,2,5,10,20,50,100)
estoque_notas = {1:n1, 2:n2, 5:n5, 10:n10, 20:n20, 50:n50, 100:n100}
valor1 = n1
valor2 = n2*2
valor5 = n5*5
valor10 = n10*10
valor20 = n20*20
valor50 = n50*50
valor100 = n100*100
totalcofre = ((valor1+valor2+valor5+valor10+valor20+valor50+valor100))

#INICIALIZAÇÃO DO "COFRE"
print(
"-------------------------" 
"\n 1 . Depositar" 
"\n 2 . Sacar" 
"\n 3 . Saldo" 
"\n 4 . Relatório" 
"\n 5 . Finalizar" 
"\n-------------------------")
opc = int(input("ESCOLHA UMA OPÇÃO: "))
while (opc != 1) and (opc != 2) and (opc != 3) and (opc != 4) and (opc != 5):
    opc = int(input("ESCOLHA UMA OPÇÃO VÁLIDA: "))
while (opc == 1) or (opc == 2) or (opc == 3) or (opc == 4) or (opc == 5):
    
# OPÇÃO 1: DEPÓSITO DE DINHEIRO
    if opc == 1:
        vaddt = 0
        rpta = 0
        print("+-- Digite 0 ou menor para encerrar o procedimento --+")
        while rpta == 0:
            vadd = int(input("Insira uma nota: "))
            if (vadd in notas) and (vadd > 0):
                vaddt += vadd
                if vadd in estoque_notas:
                    estoque_notas[vadd] += 1
                    totalcofre += vadd
            elif vadd <= 0:
                rpta += 1
            else:
                print(f"valor inválido, nota de R${vadd} não reconhecida")
        print("total adicionado: R$", vaddt)

    # OPÇÃO 2: SAQUE DE DINHEIRO
    if opc == 2:
        print("notas disponíveis:\n"
              f"-------------------------\n" 
              f" {n1} x R$1\n" 
              f" {n2} x R$2\n" 
              f" {n5} x R$5\n" 
              f" {n10} x R$10\n" 
              f" {n20} x R$20\n"
              f" {n100} x R$100\n"
              "-------------------------\n")
        
        vsac = int(input("quanto você quer sacar? "))
        if vsac <= 0:
            print("Valor de saque inválido.")
        else:
            valor_restante = vsac
            # Dicionário temporário para guardar quantas notas de cada vamos entregar
            notas_a_entregar = {}
            
            # Ordenamos as notas do maior para o menor para garantir a lógica gananciosa
            notas_disponiveis = sorted(estoque_notas.keys(), reverse=True)

            # 1. Fase de Simulação do Saque
            for nota in notas_disponiveis:
                qtd_disponivel = estoque_notas[nota]
                
                # Quantas notas deste valor nós precisaríamos teoricamente?
                qtd_necessaria = valor_restante // nota
                
                # Só podemos usar o que realmente temos no estoque
                qtd_a_usar = min(qtd_necessaria, qtd_disponivel)
                
                if qtd_a_usar > 0:
                    notas_a_entregar[nota] = qtd_a_usar
                    valor_restante -= qtd_a_usar * nota

            # 2. Validação do Sucesso
            # Se o valor restante for 0, significa que a combinação exata foi encontrada!
            if valor_restante == 0:
                # Efetiva o saque: subtrai as notas do estoque real e atualiza o total
                for nota, qtd in notas_a_entregar.items():
                    estoque_notas[nota] -= qtd
                    totalcofre -= (nota * qtd)
                    
                print(f"--- SAQUE DE R$ {vsac} APROVADO ---")
                print("Notas liberadas:")
                for nota, qtd in notas_a_entregar.items():
                    print(f"- {qtd} nota(s) de R$ {nota}")
            else:
                # Se sobrou algum valor, a combinação exata é impossível com o estoque atual
                print(f"--- ERRO NO SAQUE (R$ {vsac}) ---")
                print("Não há cédulas disponíveis para compor este valor exato.")
            
    # OPÇÃO 3: EXIBIR SALDO
    if opc == 3:

        print("-------------------------"
            f"\n {n1} x R$1" 
            f"\n {n2} x R$2" 
            f"\n {n5} x R$5" 
            f"\n {n10} x R$10" 
            f"\n {n20} x R$20"
            f"\n {n50} x R$50"
            f"\n {n100} x R$100"
            "\n-------------------------"
            f"\nO saldo atual é RS{totalcofre}")

    print(f"\nSaldo atual no sistema: R${totalcofre}")
    opc = int(input("Escolha a próxima operação (1 a 5, ou outro número para sair): "))