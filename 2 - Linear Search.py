# 05 de junho de 2019, Mateus Israel
# Linear Search

# Steps:
# 1: Pecorrer a lista
# 2: comparar o valor no indice atual com o valor que se procura

from time import sleep

lista = [8, 9, 0, 3, 4, 7, 5, 6, 1, 2]
print('A lista tem {} números!'.format(len(lista)))
val_procurado = int(input('Procurar Valor:\n'))


val_encontrado = False
val_inexistente = False
i = 0

while (val_encontrado == False and val_inexistente == False):

    if(len(lista) == i):
        val_inexistente == True
        print('\nEsse valor ({}) não existe na lista!'.format(val_procurado))
        break

    elif (lista[i] == val_procurado):
        print('Valor Encontrado: {}\n Posição(índice): {}'.format(val_procurado, i))
        val_encontrado = True

    elif(lista[i] != val_procurado):
        print('{} Não é o valor procurado'.format(lista[i]))



    
    sleep(1)
    i += 1