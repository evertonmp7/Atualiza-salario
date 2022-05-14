cont = 1

while cont <= 10:
    
    cargo = str(input('Digite seu cargo: '))
    tempo = int(input('Digite seu tempo de empresa: '))

    if cargo == "professor"  or cargo == "gerente" or cargo == "estagiário"  and tempo >=1 :
        print(cargo, 'a cima de 1 ano possui um aumento de 23% no salário')

        salario = float(input('Digite seu salário: '))
        sacomau = salario * 23 / 100
        print('Seu salário passa a ser R$', salario + sacomau)
        print('Diferença de R$', sacomau, 'a mais.')
        print('**************************************')

    else:
        print(cargo,', você não possui aumento de salário')
        print('**************************************')

    cont += 1 


