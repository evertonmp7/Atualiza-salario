placa = int(input('Digite o último numero da placa do seu veículo: '))

while placa > 9:
    print('Placa com numeração final errada! Digite novamente números entre 0 e 9: ')
    print('------------------------------------------------------')
    placa = int(input('Digite o último numero da placa do seu veículo: '))


if placa == 1 or placa == 2:

    hora = float(input('Digite o horário atual: '))

    while hora > 24:
     print('Horário não conhecido, digite novamente um horário válido entre 00.00 às 24.00')
     print('---------------------------------------------------------')
     hora = float(input('Digite o horário atual: '))

     

    if hora >= 7 and hora <= 10 or hora >= 17 and hora <= 20:
        print('Estamos no dia e hora do seu rodizio, cuidado')

    elif hora >= 0 and hora <= 7:
        print('Hoje é o seu rodizio. Atenção, ele começa a partir das 7:00 finaliza às 10:00 e retorna às 17:00 e finaliza às 20:00')

    elif hora > 10.10 and hora < 17:
        print('Hoje é o seu rodizio, mas nesse horário você pode circular até às 17:00 e depois das 20:10')

    elif hora > 20.10 and hora <= 24:
        print('Hoje é seu rodizio, mas o horário de restrição finalizou às 20:10')

     

else:
    print('Hoje não é o seu rodízio!')








    
