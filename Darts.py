def score(x, y):
    a = x ** 2 + y ** 2
    print(a)
    if(a <= 1):
        return 10
    elif (a <= 25):
        return 5
    elif (a <= 100):
        return 1
    else:
        return 0
if __name__ == '__main__':

    # print(add_prefix_un(input("Enter number: ")))
    print(f'Wynik: {score(150, 0.5)}')