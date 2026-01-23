def text_indentation(text):
    """
    Prints text with a newline after each '.', '?', or ':', without extra blank lines.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            # Only print a single newline
            if i != len(text) - 1:
                print()
        i += 1
