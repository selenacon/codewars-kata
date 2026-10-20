def alphabet_position(text):
    import string
    alphabetPositions = ""
    for char in text.lower().replace(' ',''):
        if char.isalpha():
            alphabetPositions += str(string.ascii_lowercase.index(char) + 1) + ' '
    return alphabetPositions.rstrip()