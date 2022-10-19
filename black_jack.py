"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """

    if (card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']):
        return int(card)
    elif(card in ['J', 'Q', 'K']):
        return 10
    elif(card == 'A'):
        return 1

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if(value_of_card(card_one) > value_of_card(card_two)):
        return card_one
    if(value_of_card( card_one ) < value_of_card( card_two )):
        return card_two
    else:
        return card_one, card_two



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    if((value_of_card(card_one) + value_of_card(card_two)+ 11) <= 21):
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    if(card_one == 'A' and card_two in ['J','Q', 'K','10']):
        return True
    elif(card_two == 'A' and card_one in ['J','Q', 'K','10']):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    print([(value_of_card(card_one) in [1, 9, 10,]), value_of_card(card_two) in [9, 10, 1]])
    if(value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11] ):
        return True
    else:
         return False
if __name__ == '__main__':
    # print(add_prefix_un(input("Enter number: ")))
    print( f"Card POWER: {value_of_card('A')}" )
    print( f"Higher card: {higher_card('A', 'K')}" )
    print( f"Higher card: {value_of_ace('7', '3')}" )
    print( f"is_blackjack: {is_blackjack('9', 'A')}" )
    print( f"Split pairs: {can_split_pairs('10', 'K')}" )
    print( f"double down: {can_double_down('10', '9')}" )