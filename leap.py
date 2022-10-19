def leap_year(year):
    x = year % 4
    print(x)
    if(x == 0 and year % 100 != 0):
        return True
    elif(x == 0 and year % 400 == 0):
        return True
    else:
        return False


if __name__ == '__main__':

    # print(add_prefix_un(input("Enter number: ")))
    print(f'Wynik: {leap_year(1900)}')