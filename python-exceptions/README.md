# Python - Exceptions

Gestion des erreurs en Python : blocs try/except, types d'exceptions et levée d'exceptions personnalisées.

## Utilisation

```bash
python3 <fichier>.py
```

## Tâches

| Fichier | Fonction | Description |
| ------- | -------- | ----------- |
| `0-safe_print_list.py` | `safe_print_list(my_list, x)` | Affiche `x` éléments d'une liste en sécurisant les erreurs d'index |
| `1-safe_print_integer.py` | `safe_print_integer(value)` | Affiche une valeur avec `{:d}` si c'est un entier, `False` sinon |
| `2-safe_print_list_integers.py` | `safe_print_list_integers(my_list, length)` | Affiche les entiers d'une liste, ignore silencieusement les autres types |
| `3-safe_print_division.py` | `safe_print_division(a, b)` | Divise deux entiers en gérant `ZeroDivisionError`, affiche le résultat dans `finally` |
| `4-list_division.py` | `list_division(my_list_1, my_list_2, list_length)` | Divise deux listes élément par élément avec gestion de toutes les erreurs possibles |
| `5-raise_exception.py` | `raise_exception()` | Lève une `TypeError` |
| `6-raise_exception_msg.py` | `raise_exception_msg(message)` | Lève une `NameError` avec un message personnalisé |

## Concepts clés

- Bloc `try` / `except` / `else` / `finally`
- Types d'exceptions standard : `TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`, `NameError`
- Instruction `raise` pour lever une exception manuellement
- Clause `finally` — s'exécute toujours, même en cas d'exception
- Vérification de type avec `isinstance()`
- Gestion silencieuse des erreurs (ignorer et continuer)
