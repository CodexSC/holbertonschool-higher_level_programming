#!/usr/bin/node

// fonction addition visible depuis l'extérieur
function add(a, b) {
  return a + b;
}

// exporter la fonction
module.exports.add = add;
