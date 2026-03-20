#!/usr/bin/python3

# Divise les éléments en paires d'index entre deux listes en gérant les erreurs
def list_division(my_list_1, my_list_2, list_length):  # Définit la fonction 'list_division'
    """Retourne une liste de divisions élément par élément entre `my_list_1` et `my_list_2`.

    Pour chaque index i dans [0, list_length), effectue my_list_1[i] / my_list_2[i] en gérant:
      - IndexError lorsque les listes sont trop courtes
      - ValueError lorsque les éléments ne sont pas numériques
      - ZeroDivisionError lorsque le diviseur est 0
    Les erreurs sont affichées et la valeur 0 est ajoutée au résultat pour cet index.
    """
    result = []  # Liste des résultats
    for i in range(list_length):  # Pour chaque index demandé
        try:  # Essaye d'effectuer la division
            if i >= len(my_list_1) or i >= len(my_list_2):  # Vérifie la présence des éléments
                raise IndexError("out of range")
            element_1 = my_list_1[i]  # Récupère l'élément de la première liste
            element_2 = my_list_2[i]  # Récupère l'élément de la seconde liste
            # Vérifie que les deux éléments sont numériques (int ou float)
            if not isinstance(element_1, (int, float)) or \
                    not isinstance(element_2, (int, float)):
                raise ValueError("wrong type")
            if element_2 == 0:  # Division par zéro
                raise ZeroDivisionError("division by 0")
            division_result = element_1 / element_2  # Effectue la division
        except IndexError as e:  # Liste trop courte
            print(e)  # Affiche l'erreur
            division_result = 0
        except ValueError as e:  # Mauvais type
            print(e)  # Affiche l'erreur
            division_result = 0
        except ZeroDivisionError as e:  # Division par zéro
            print(e)  # Affiche l'erreur
            division_result = 0
        finally:  # Ajoute le résultat calculé (ou 0 en cas d'erreur)
            result.append(division_result)  # Code
    return result  # Retourne le résultat
