#!/usr/bin/python3

# Retourne l'élément situé à l'index `idx` dans `my_list` ou `None` si l'index est invalide
def element_at(my_list, idx):  # Définit la fonction 'element_at'
    """Retourne l'élément à l'index spécifié dans la liste `my_list`.

    :param my_list: La liste d'éléments.
    :type my_list: list

    :param idx: L'index de l'élément à retourner.
    :type idx: int

    :return: L'élément à l'index spécifié ou None si l'index est invalide.
    :rtype: Any or None
    """
    # Si l'index est négatif, on considère l'index invalide
    if idx < 0:  # Condition si
        return None  # Retourne le résultat

    # Si l'index dépasse la longueur de la liste, on retourne None
    if idx >= len(my_list):  # Condition si
        return None  # Retourne le résultat

    # Sinon, retourne l'élément demandé
    return my_list[idx]  # Retourne le résultat


# Exemple d'utilisation
if __name__ == "__main__":  # Condition si
    my_list = [1, 2, 3, 4, 5]  # Affecte une valeur à 'my_list'
    try:  # Bloc try pour démonstration
        # Accès valide
        print(element_at(my_list, 2))  # Affiche 3        # Affiche à l'écran
        # Accès invalide (index négatif) — retourne None
        print(element_at(my_list, -1))  # Affiche None        # Affiche à l'écran
        # Accès invalide (index hors limite) — retourne None
        print(element_at(my_list, 10))  # Affiche None        # Affiche à l'écran
    except IndexError as e:  # Capture l'exception si elle survenait
        print(e)  # Affiche à l'écran
