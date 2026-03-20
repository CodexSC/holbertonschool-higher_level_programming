#!/usr/bin/python3
"""Module définissant `VerboseList`, une liste avec notifications de modification."""


class VerboseList(list):
    """Sous-classe de `list` qui logge les opérations mutantes.

    Chaque opération modifiante imprime un message décrivant l'action.
    """

    def append(self, item):
        """Ajoute un élément et affiche une notification.

        Args:
            item: élément à ajouter.
        """
        super().append(item)
        # Message informatif indiquant l'ajout
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étend la liste avec les éléments fournis et notifie l'utilisateur.

        Args:
            iterable: itérable d'éléments à ajouter.
        """
        items = list(iterable)
        super().extend(items)
        # Indique le nombre d'éléments ajoutés
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Supprime un élément et affiche une notification.

        Args:
            item: élément à supprimer.
        """
        # Affiche d'abord le message, puis effectue la suppression
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Supprime et renvoie l'élément à l'index, en notifiant.

        Args:
            index: position de l'élément à retirer (par défaut : -1).

        Returns:
            L'élément qui a été retiré.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
