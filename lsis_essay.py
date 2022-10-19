def capitalize_title(title):
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """


    return title.title()

def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """

    return sentence.replace(old_word, new_word)


if __name__ == '__main__':

    # print(add_prefix_un(input("Enter number: ")))
    print(f'Capitalized title: {capitalize_title("lubie placki")}')
    print(f'Is dot in the end>: {check_sentence_ending("The quick brown fox jumped over the lazy dog")}')
    print(f'Without spaces>: {clean_up_spacing(" I like to go on hikes with my dog.  ")}')
    print(f"Synonym>: {replace_word_choice('bookkeeper', 'kk', 'k  k')}")