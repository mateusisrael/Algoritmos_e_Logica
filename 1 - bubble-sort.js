/* 
OBS> Preciso organizar a lista: step 3

1 de junho de 2019, Mateus Israel
Praticando algoritmos e lógica
Bubble Sort

Steps
1: Setar a posição das 'pás'.
2: Percorrer a lista da direita para a esquerda.
3: Inverter as posiões dos números na posição errada

*/

'use strict';

// numeros
var numeros = [1, 3, 4, 8, 7, 6, 2, 5, 9];



var fora_de_ordem = true;
while(fora_de_ordem) {

    // step 1
    var p_dir = numeros.length - 1;
    var p_esq = numeros.length -2;


    fora_de_ordem = false

    // step 2
    while (p_esq >= 0) {
        console.log(`${numeros[p_esq]} - ${numeros[p_dir]}: `)
    
        if (numeros[p_dir] < numeros[p_esq]) {
            console.log(`Seletor à ESQUERDA maior que o a DIREITA`);
            
            // step 3
            var v_repozic = numeros[p_esq];
            // inserir o v_repozic à direita da p_dir
            numeros.splice(p_esq);
            console.log(`Reposição ${numeros}`);

            fora_de_ordem = true;
        }
    
        p_esq -= 1;
        p_dir -= 1;
    }

}


