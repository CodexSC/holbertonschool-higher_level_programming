#!/usr/bin/node

// fonction qui additionne deux nombres
function add(a, b) {
  return a + b;
}

// récupérer les deux arguments et les convertir en entier
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

console.log(add(num1, num2)); // afficher le résultat
