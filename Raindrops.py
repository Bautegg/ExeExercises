def convert(number):
    return "".join(s for mod, s in [(3, "Pling"), (5, "Plang"), (7, "Plong")]
                   if number % mod == 0) or str(number)


if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'Raindrops: {convert(15)}' )