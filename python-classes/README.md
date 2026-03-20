# Python - Classes and Objects

Introduction à la programmation orientée objet (POO) en Python : définition de classes, attributs et méthodes.

## Utilisation

```bash
python3 <N>-main.py
```

## Tâches

Les tâches construisent progressivement une classe `Square` :

| Fichier | Contenu |
| ------- | ------- |
| `0-square.py` | Classe `Square` vide |
| `1-square.py` | Classe `Square` avec attribut privé `__size` |
| `2-square.py` | Ajout de la validation du type et de la valeur de `size` dans `__init__` |
| `3-square.py` | Ajout de la méthode `area()` qui retourne l'aire du carré |
| `4-square.py` | Ajout de la propriété `size` avec `@property` et `@size.setter` |
| `5-square.py` | Ajout de la méthode `my_print()` qui affiche le carré avec `#` |
| `6-square.py` | Ajout de l'attribut `position` (tuple) pour contrôler le décalage à l'affichage |

## Progression des concepts

```python
# 0: class Square: pass
# 1: def __init__(self, size): self.__size = size
# 2: + validation TypeError/ValueError dans __init__
# 3: + def area(self): return self.__size ** 2
# 4: + @property / @size.setter
# 5: + def my_print(self): affichage en #
# 6: + position = (x, y) pour le décalage
```

## Concepts clés

- Définition de classe avec `class`
- Constructeur `__init__` et `self`
- Attributs privés avec préfixe `__` (name mangling)
- **Propriétés** : `@property` (getter) et `@attribut.setter` (setter)
- Validation de type avec `isinstance()` et levée de `TypeError` / `ValueError`
- Méthodes d'instance
- Méthode spéciale `__str__` pour la représentation en chaîne
