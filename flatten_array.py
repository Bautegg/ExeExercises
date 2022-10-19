def flatten(iterable):
    A = []
    for element in iterable:
        if isinstance(element, list):
            A += flatten(element)
        elif element ==  None:
            continue
        else:
            A.append(element)
    return A
def czylista(iterable):
    B = []
    for element in iterable:
        B.append(isinstance(element, list))
    return B

if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'list: {flatten([1,[2,3, None,4],[],5])}' )
    print( f'czy lista: {czylista([1,[2,3, None,4],[],5])}' )