# Python - Data Structures: Lists, Tuples

Manipulation des structures de données séquentielles en Python : listes et tuples.

## Utilisation

```bash
python3 <N>-main.py
```

## Tâches

| Fichier | Fonction | Description |
| ------- | -------- | ----------- |
| `0-print_list_integer.py` | `print_list_integer(my_list)` | Affiche chaque entier de la liste avec `{:d}` |
| `1-element_at.py` | `element_at(my_list, idx)` | Retourne l'élément à l'index `idx`, `None` si invalide |
| `2-replace_in_list.py` | `replace_in_list(my_list, idx, element)` | Remplace un élément en place |
| `3-print_reversed_list_integer.py` | `print_reversed_list_integer(my_list)` | Affiche la liste en ordre inverse |
| `4-new_in_list.py` | `new_in_list(my_list, idx, element)` | Remplace sans modifier la liste originale (copie) |
| `5-no_c.py` | `no_c(my_string)` | Retourne la chaîne sans les lettres `c` et `C` |
| `6-print_matrix_integer.py` | `print_matrix_integer(matrix)` | Affiche une matrice 2D ligne par ligne |
| `7-add_tuple.py` | `add_tuple(tuple_a, tuple_b)` | Additionne deux tuples élément par élément (2 premiers) |
| `8-multiple_returns.py` | `multiple_returns(sentence)` | Retourne `(longueur, premier_caractère)` |
| `9-max_integer.py` | `max_integer(my_list)` | Retourne le plus grand entier, `None` si vide |
| `10-divisible_by_2.py` | `divisible_by_2(my_list)` | Retourne une liste de booléens (divisible par 2 ?) |
| `11-delete_at.py` | `delete_at(my_list, idx)` | Supprime l'élément à l'index `idx` (en place) |
| `12-switch.py` | — | Échange les valeurs de deux variables `a` et `b` |

## Concepts clés

- **Listes** : création, accès par index, modification en place, suppression (`del`)
- **Slicing** : `liste[debut:fin:pas]`, copie avec `liste[:]`
- **Tuples** : immuables, unpacking, accès par index
- Opérations destructives vs non-destructives
- Itération et compréhensions de listes
- Fonction `map()` avec lambda
- Échange de variables : `a, b = b, a`
