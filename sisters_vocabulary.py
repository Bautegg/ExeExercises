def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    unword = 'un' + word
    return unword


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """


    return (' :: ' + vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    word = word[:-4]
    print(word)

    if('i' == word[-1]):
        print('Y works')
        word = word[:-1] + "y"
        print(f'word:  {word}')
    else:
        print('Y dont works')

    return word


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    word = (sentence.split()[index])
    if(word[-1] == '.'):
        print(word)
        word = word[:-1]
    return word + 'en'
if __name__ == '__main__':

    # print(add_prefix_un(input("Enter number: ")))
    print(add_prefix_un("healthy"))
    print(make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete','echolalia', 'encoder', 'biography']))
    print(remove_suffix_ness('artiness'))
    print(adjective_to_verb('The butter got soft in the sun.', 2 ))