print('Esse programa foi definido para repetir até no máximo 10 vezes a tabuada desejada')
print('*********************************************************************************')



tabu = int(input('Digite o número da tabuada desejada: '))
cont = 1

while cont <= 10:

     resul = tabu * cont

     print(tabu, 'x', cont, '=', resul)

     cont = cont + 1
    

maximo = 1

while maximo <= 10:

    print('-----------------------')
    print('Gostaria de continuar?')
    continuar = int(input('Digite 1 para sim ou 2 para não: '))
    print('-----------------------')

    if continuar == 1:


        tabu = int(input('Digite o número da tabuada desejada: '))

        cont = 1

        while cont <= 10:

            resul = tabu * cont

            print(tabu, 'x', cont, '=', resul)


            cont += 1
        
    else:
        print('Até logo!')


    maximo += 1

break




        

        






    

    

    
