#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg# Affecte une valeur à 'raise_exception_msg'

try:# Bloc try
    raise_exception_msg("C is fun")    # Code
except NameError as ne:# Capture l'exception
    print(ne)    # Affiche à l'écran
