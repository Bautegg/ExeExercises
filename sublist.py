"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
# SUBLIST = None
# SUPERLIST = None
# EQUAL = None
# UNEQUAL = None


SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)
def sublist(list_one, list_two):
    L1 = str(list_one)[1:-1]
    L2 = str(list_two)[1:-1]
    print(L1)
    print(L2)
    if L1 == L2:
        return EQUAL
    # for i in range(0,len(list_one)):
    #     print(list_one[i])
    #     if list_one[i] == list_two[i]:
    #         print(True)
    #     else:
    #         print(list_one[i] == list_two[i+1])
    elif L1 in L2:
        return SUBLIST
    elif L2 in L1:
        return SUPERLIST
    else:
        return UNEQUAL

if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'Lists are: {sublist([1, 2],[1, 22])}' )