#!/usr/bin/node

// fonction récursive pour calculer le factoriel
function factorial(n) {
  if (n <= 1 || isNaN(n)) {
    return 1; // factoriel de 0 ou NaN
  }
  return n * factorial(n - 1); // appel récursif
}

// récupérer le premier argument et le convertir en entier
const num = parseInt(process.argv[2]);

console.log(factorial(num)); // afficher le résultat
