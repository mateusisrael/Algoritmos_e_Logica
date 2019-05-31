'use strict';

// lista
var lista = [1, 3, 2, 5, 10];
var p_dir = lista.length - 1;
var p_esq = lista.length -2;
console.log(p_dir);
/*
while (p_esq >= 0) {
    console.log(`${lista[p_esq]} - ${lista[p_dir]}: `)

    if (lista[p_dir] < lista[p_esq]) {
        console.log(`Seletor à ESQUERDA maior que o a DIREITA`);

        console.log(`${lista} \n`);
    }
    p_esq -= 1;
    p_dir -= 1;
}
*/
