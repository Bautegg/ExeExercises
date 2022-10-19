"""
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.

The alphabet used consists of letters a to z, inclusive, and is case insensitive.
"""

#20.08.22

def is_pangram(sentence):
    # import string #do wygenerowania listy alfabetu
    # alphabet = list(string.ascii_lowercase)
    # return alphabet
    a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    print(f'znaki w alfabecie: {len( a_list )}')
    print(f'znaki w zdaniu: {len( sentence )}')
    print(sentence.isalpha())
    # i = -1
    # j = 0
    # while i < 25:
    #
    #     i += 1
    #     print( i )
    #     a_ch = a_list[i]
    #
    #     print(f'** a_ch: {a_ch}**')
    #     for element in range(j, len(sentence)):
    #         s_ch = sentence[element]
    #         print(f' s_ch: {s_ch}')
    #         j += 1
    #         if a_ch == s_ch:
    #             a_list.pop( i )
    #             print('pop', a_list)
    #             break
    sentence = sentence.lower()
    print(sentence)
    for s_ch in sentence: #pętla przeszukująca stringa
        print(f' s_ch: **{s_ch}**')
        for a_ch in a_list: #pętla przeszukująca alfabet
            print(f'a_ch: {a_ch}')
            if a_ch==s_ch:
                a_list.remove(a_ch)
                print('pop', a_list)
                break
    if a_list == []:
        return True
    else:
        return False




if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print( f"*is pangram?: {is_pangram('Five quacking Zephyrs jolt my wax bed.')}*" )
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')