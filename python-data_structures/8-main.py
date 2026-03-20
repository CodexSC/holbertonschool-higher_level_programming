#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns# Affecte une valeur à 'multiple_returns'

sentence = "At school, I learnt C!"# Affecte une valeur à 'sentence'
length, first = multiple_returns(sentence)# Affecte une valeur à 'first'
print("Length: {:d} - First character: {}".format(length, first))# Affiche à l'écran
