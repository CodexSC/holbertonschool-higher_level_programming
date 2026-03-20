#!/usr/bin/node

// récupérer tous les arguments et les convertir en entiers
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0); // 0 si aucun ou un seul argument
} else {
  // trier par ordre décroissant
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]); // afficher le deuxième plus grand
}
