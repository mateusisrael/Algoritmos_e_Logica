# 30 de maio de 2019, Mateus Israel,

# Praticando Algoritmos e lógica de programação.
# Bubble Sort

# Steps:
# 1: seta a posição das 'pás'.
# 2: Percorrer a lista da direita para a esquerda.
# 3: Inverter as posiões dos números na posição errada.

from time import sleep


numeros = [1, 3, 4, 8, 7, 6, 2, 5, 9]       # lista com os números fora de ordem.
print('Lista original: {}\n'.format(numeros))



fora_de_ordem = True
while(fora_de_ordem):

    # step 1
    p_dir = len(numeros) - 1                    # A 'pá direita' inicia ao final da lista.
    p_esq = len(numeros) - 2                    # A 'pá esquerda' inicia ao final da lista, a esquerda da pá direita.
    
    
    fora_de_ordem = False

    # step 2
    while(p_esq >= 0):
        print('p_esq: {} - p_dir: {}'.format(numeros[p_esq], numeros[p_dir]))

        if(numeros[p_esq] > numeros[p_dir]):
            print('p_esq > p_dir')

            # step 3:
            v_repozic = numeros[p_esq]
            numeros.insert(p_dir + 1, v_repozic)
            numeros.pop(p_esq)
            print('REPOSIÇÃO: {} \n'.format(numeros))
            
            fora_de_ordem = True


        p_esq = p_esq - 1
        p_dir = p_dir - 1

        sleep(0.5)
