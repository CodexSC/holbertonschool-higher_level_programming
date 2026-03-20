# Python - Abstract Classes and Interfaces

Classes abstraites, duck typing, mixins et protocoles itérateurs en Python.

## Utilisation

```bash
python3 main_<N>_<nom>.py
```

## Tâches

| Fichier | Contenu |
| ------- | ------- |
| `task_00_abc.py` | Classe abstraite `Animal` avec méthode abstraite `sound()` ; implémentations `Dog` et `Cat` |
| `task_01_duck_typing.py` | Duck typing : classe `Shape` abstraite avec `area()` et `perimeter()` ; `Circle` et `Rectangle` |
| `task_02_verboselist.py` | Classe `VerboseList(list)` qui affiche un message à chaque `append`, `extend`, `remove`, `pop` |
| `task_03_countediterator.py` | Classe `CountedIterator` qui encapsule un itérateur et compte les éléments parcourus |
| `task_04_flyingfish.py` | Héritage multiple : `FlyingFish(Fish, Bird)` avec `FlyMixin` et `SwimMixin` ; MRO |
| `task_05_dragon.py` | Design par mixins : `Dragon` hérite de `SwimMixin` et `FlyMixin` avec `roar()` |

## Concepts clés

- **Module `abc`** : `ABC`, `@abstractmethod` — empêche l'instanciation de la classe abstraite
- **Duck typing** — "Si ça nage et cancane, c'est un canard" : l'interface prime sur le type réel
- **Mixins** — classes légères ajoutant un comportement spécifique via héritage multiple
- **Protocole itérateur** : `__iter__()` et `__next__()` avec `StopIteration`
- **MRO** (Method Resolution Order) : ordre de résolution des méthodes avec `__mro__` ou `mro()`
- Surcharge de méthodes de liste (`append`, `extend`, `remove`, `pop`)
