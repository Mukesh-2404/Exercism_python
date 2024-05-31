def is_valid(isbn):
    isbn = isbn.replace("-", "").upper()

    if len(isbn) != 10:
        return False
 
    total = 0
    for i, char in enumerate(isbn[:-1]):
        if char.isdigit():
            total += int(char) * (10 - i)
        else:
            return False 

    last_char = isbn[-1]
    if last_char.isdigit():
        total += int(last_char)
    elif last_char == 'X':
        total += 10
    else:
        return False  

    return total % 11 == 0
    pass
