#!/usr/bin/python3

# Imprime une matrice d'entiers avec les lignes sur des lignes séparées
def print_matrix_integer(matrix=[[]]):  # Définit la fonction 'print_matrix_integer'
    """Imprime une matrice d'entiers avec chaque élément séparé par un espace et les lignes séparées par un saut de ligne.

    :param matrix: La matrice d'entiers à imprimer. Par défaut, une matrice vide.
    :type matrix: list of list

    :return: Aucune valeur de retour
    :rtype: None
    """
    # Parcourt chaque ligne de la matrice
    for row in matrix:  # Boucle pour
        # Parcourt chaque élément de la ligne en connaissant son index
        for i, num in enumerate(row):  # Boucle pour
            # Si ce n'est pas le dernier élément de la ligne, ajoute un espace après
            if i < len(row) - 1:  # Condition si
                print("{:d}".format(num), end=" ")  # Affiche à l'écran
            else:  # Sinon (dernier élément)
                print("{:d}".format(num), end="")  # Affiche à l'écran
        # Passe à la ligne suivante après avoir imprimé tous les éléments d'une ligne
        print()  # Affiche à l'écran
