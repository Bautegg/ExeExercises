def color_code(color):
    return colors().index(color)



def colors():
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

if __name__ == '__main__':
    # print(add_prefix_un(input("Enter number: ")))
    print( f"Band Value: {color_code('white')}" )