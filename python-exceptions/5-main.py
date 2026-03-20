#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception# Affecte une valeur à 'raise_exception'

try:# Bloc try
    raise_exception()    # Code
except TypeError as te:# Capture l'exception
    print("Exception raised")    # Affiche à l'écran
