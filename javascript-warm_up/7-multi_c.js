#!/usr/bin/node

// récupérer le premier argument et le convertir en entier
const times = parseInt(process.argv[2]);

// vérifier si c'est un nombre valide
if (isNaN(times) || times <= 0) {
  console.log('Missing number of occurrences'); // message d'erreur
} else {
  // boucle pour afficher "C is fun" times fois
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
