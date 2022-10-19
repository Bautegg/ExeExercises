def translate(text):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
     # vowels = {'a', 'e', 'i', 'o', 'u'}
     # print(text[0:2])
     # print( f'{text[3:]} + {text[0:3]} + ay, {text[2:4]}' )
     #
     # if text[0] in vowels or text[0:2] == 'xr' or text[0:2] == 'yt': #Czy pierwsza litera jest samogłoską?
     #     return text + 'ay'
     # else:
     #     if text[1] not in vowels: #Czy druga litera nie jest samogłoską
     #         if text[2:4] == 'qu':
     #             return text[4:] + text[0:4] + 'ay'
     #
     #         return text[2:] + text[0:2] + 'ay'
     #     elif text[1:3] == 'qu':
     #         return text[3:] + text[0:3] + 'ay'
     #     return text[1:] + text[0] + 'ay'





    # print(text[2:], text[0:2])




if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print( f"Pig Latin: {translate('square')}" )
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')