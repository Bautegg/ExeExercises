"""Functions to keep track and alter inventory."""

# ['coal', 'iron', 'iron','mom']
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    stuff = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
    dict_stuff = {}
    print(stuff)
    dict_stuff.setdefault('cos')
    print(dict_stuff)


    0
    # inventory = dict(coal=5, iron=1, suply=True)
    # inventor = {}
    # for i in items: #pętla do przeszukiwania słownika inventory
    #     print( f'i: {i}' )
    #     for x in inventory: #pętla do przeszukiwania listy items
    #
    #         print(f'i, x: {i, x}')
    #
    #         if x == i:
    #             inventory.setdefault(i, 1)
    #             element = inventory[x] + 1
    #             print( f'inventory2:  {x, element}' )
    #             print( inventory )
    #             continue

    # inventory = {}
    # Li = len(items)
    # for i in range(0, Li):
    #     element = items[i]
    #     print( f'element: {element}' )
    #     inventory.setdefault(element, 1)
    #     print( inventory )
    #     k = list( inventory.keys() )[-1]
    #     print(f' k: {k}')
    #     if k == element:
    #         inventory[k] += 1

    inventory = {}

    # for i in items:
    #     print( f'i: {i}' )
    #     element = inventory.setdefault( i, 1 )
    #
    #     print( f'inventory: {inventory}' )
    #     return element






def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    pass


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    pass


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    pass


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass


if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print(f"steps: {create_inventory(['coal', 'coal', 'iron','coal','mom'])}")
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')