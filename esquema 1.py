#DEFINIÇÃO DA QUANTIDADE DE DINHEIRO E VALOR INVIDUAL E TOTAL
n1 = n2 = n5 = n10 = n20 = n50 = n100 = 2
valor1 = n1
valor2 = n2*2
valor5 = n5*5
valor10 = n10*10
valor20 = n20*20
valor50 = n50*50
valor100 = n100*100
notas = (1,2,5,10,20,)
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

#DEPÓSITO DE DINHEIRO
if opc == 1:
    vaddt = 0
    rpta = 0
    print("+-- Digite 0 ou menor para encerrar o procedimento --+")
    while rpta == 0:
        vadd = int(input("Insira uma nota: "))
        if (vadd in notas) and (vadd > 0):
            vaddt += vadd
        elif vadd <=0:
            rpta+=1
        else:
            print(f"valor inválido, nota de R${vadd} não reconhecida")
    print("total adicionado: R$",vaddt)

#SAQUE DE DINHEIRO
if opc == 2:
    print("notas disponívveis:\n"
f"-------------------------\n" 
f" {n1} x R$1\n" 
f" {n2} x R$2\n" 
f" {n5} x R$5\n" 
f" {n10} x R$10\n" 
f" {n20} x R$20\n"
f" {n100} x R$100\n"
"-------------------------\n")
    vsac = int(input("QUANTO VOCÊ QUER RETIRAR? "))
    for x in notas:
        sobra =vsac % x

    rg1 = totalcofre%100
    if rg1 >= 0.5:
        rg2 = rg1*100%50
    elif rg1 >= 0.2:
        rg2 = rg1*100%20
    elif rg1 >= .1:
        rg2 = rg1*100%10
    elif rg1>= .05:
        rg2 = rg1*100%5
    elif rg1>= .02:
        rg2 = rg1*100%2
    else: rg2 = rg1*100
    

    while (vsac > totalcofre) and (sobra != 0):
        print(f"Não é possível retirar R${vsac}")
    
print(totalcofre)
