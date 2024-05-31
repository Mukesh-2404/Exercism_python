# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'

def sub_super(one,two):
    for i in range(len(one)-len(two)+1):
        if not two or one[i:i+len(two)]==two:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif sub_super(list_one, list_two):
        return SUPERLIST
    elif sub_super(list_two, list_one):
        return SUBLIST
    return UNEQUAL