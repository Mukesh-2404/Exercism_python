def square(number):
    if 1<=number<=64:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")
    pass

def total():
    return sum (square(number) for number in range(1, 65))
    pass
