def square(number):
    if(number > 64 or number < 1):
        raise ValueError("square must be between 1 and 64")
    import math
    return math.pow(2, number - 1)


def total():
    number2 = 0
    for x in range(64):

        print(f'x= {x}')
        print(f"number2= {number2}")

        import math
        number2 = number2 + math.pow(2, x)
        print(f"potęga= {math.pow(2, x)}")
        print(number2)
    return int(number2
if __name__ == '__main__':
    print(square(int(input("Enter number: "))))
    print(total())