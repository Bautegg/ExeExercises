def add(moment):
    import datetime
    gigasecond = datetime.timedelta(seconds=10**9)
    return moment + gigasecond


if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'moment: {add(2021, 5, 17)}' )