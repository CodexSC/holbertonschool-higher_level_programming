#!/usr/bin/node

// récupérer le premier argument et convertir en entier
const size = parseInt(process.argv[2]);

// vérifier si c'est un nombre valide
if (isNaN(size) || size <= 0) {
  console.log('Missing size'); // message d'erreur
} else {
  // construire chaque ligne du carré
  const line = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(line); // afficher la ligne
  }
}
