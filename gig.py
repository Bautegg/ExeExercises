def add(moment):

    gigasecond = datetime.timedelta(seconds=10**9)

    return moment + gigasecond


if __name__ == '__main__':
    import datetime
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'moment: {add(datetime.datetime(2023, 5, 17, 0, 0))}' )