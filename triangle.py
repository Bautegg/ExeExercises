def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0:
        return a == b and b == c
    else:
        print("co to za dane ciulu równoboczny?")
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        return a==b or b==c or a==c
    else:
        print( "co to za dane ciulu równoramienny?" )
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        return a!=b and b!=c
    else:
        print( "co to za dane ciulu różnoboczny?" )
        return False

if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'Czy rónoboczny?: {equilateral([0, 5, 5])}' )
    print( f'Czy równoramienny?: {isosceles([6, 10, 6])}' )
    print( f'Czy różnoboczny?: {scalene([40, 40.5, 6])}' )