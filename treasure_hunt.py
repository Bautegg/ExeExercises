def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record) == True:
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    list = []
    for element in combined_record_group:
        list.append(f"{element[0] , element[2], element[3], element[4]}\n")
    return "".join(list)

if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    print( f'get coordinate: {get_coordinate(("Scrimshaw Whales Tooth", "2A"))}' )
    print( f"convert_coordinate: {convert_coordinate('2A')}" )
    print( f"compare records: {compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))}" )
    print( f"create_record: {create_record(('Model Ship in Large Bottle', '9A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))}" )
    print( f"clean_up: {clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))}" )
