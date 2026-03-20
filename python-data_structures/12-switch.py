#!/usr/bin/python3

# Échange les valeurs des variables a et b
# Affecte des valeurs initiales
a = 89  # Affecte une valeur à 'a'
b = 10  # Affecte une valeur à 'b'

# Effectue l'échange en utilisant la destructuration (multiple assignment)
# Après cette ligne, 'a' prend la valeur précédente de 'b' et vice-versa
a, b = b, a  # Affecte une valeur à 'b'

# Affiche les nouvelles valeurs de a et b au format décimal
print("a={:d} - b={:d}".format(a, b))  # Affiche à l'écran
