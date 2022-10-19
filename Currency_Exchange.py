def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    x = exchange_rate * spread /100
    print(f"Tyle wynosi x: {x}" )
    nowy_budzet = exchange_money(budget, exchange_rate * (spread /100+1))
    ile_banknotow = get_number_of_bills(nowy_budzet, denomination)
    return get_value_of_bills(denomination, ile_banknotow)



def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spnread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    nowy_budzet = exchange_money(budget, exchange_rate * (spread / 100 + 1))
    po_wymianie = nowy_budzet - exchangeable_value(budget, exchange_rate, spread, denomination)
    return int(po_wymianie)


if __name__ == '__main__':
    # print(exchange_money(int(input("Enter budget: ")), 2))
    # print(get_change(int(input("Enter budget2: ")), 3))
    # print(get_number_of_bills(int(input("Enter budget3: ")),int(input("Enter denomination: "))))
    # budget = float(input("budget: "))
    # exchange_rate = float(input("exchange rate: "))
    # spread = int(input("spread: "))
    # denomination = int(input("denomination: "))
    # print(exchangeable_value(budget,exchange_rate, spread, denomination))
    # print(non_exchangeable_value(budget, exchange_rate, spread, denomination))
    print(get_change(463000, 5000))

