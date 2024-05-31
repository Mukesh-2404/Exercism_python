def is_isogram(string):
    string=string.lower()
    unique_letters = set()
    
    for char in string:
        if char.isalpha():
            if char in unique_letters:
                return False
            unique_letters.add(char)
    return True

    pass
