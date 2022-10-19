def square(number):
    if(number > 64 or number < 1):
        raise ValueError("square must be between 1 and 64")
    import math
    return math.pow(2, number - 1)


def total():

    return 2 ** 64 -1

if __name__ == '__main__':

    print(square(int(input("Enter number: "))))
    print(total())
