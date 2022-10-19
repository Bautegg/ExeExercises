def is_isogram(string):
    string = string.lower()
    print(string)
    i = 0
    for ch1 in string:
        i += 1
        if ch1.isalpha():
            print('ch1: ', ch1,'*')
            for element in range(i,len(string)):
                ch2 = string[element]
                print('ch2: ', ch2)
                print( 'i: ', i )
                if ch1 == ch2:
                    return False
        else:
            continue
    return True





if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print( f"*is isogram?: {is_isogram('  ab-  cd-e  ')}*" )
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')