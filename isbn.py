def is_valid(isbn):

    c=10 #licznik
    isbn = ''.join(char for char in isbn if char.isalnum())
    print(isbn)
    if len( isbn )==10: # jeżeli długość stringa isbn wynosi 10 znaków:
        if isbn[0:-1].isdigit(): # jeżeli pierwsze 9 znaków to cyfry:
            print(isbn[0:-1])
            print('isbn2',isbn)
            if  isbn[-1] == 'X' : #jeżeli ostatni znak stringa isbn to 'X'
                print( 'isbn[-1]', isbn[-1] )
                sum = 10
                print('sum if: ',sum)
                isbn = isbn[:-1:] #usuń ostatni znak stringa isbn
            elif isbn[-1].isdigit():
                sum = 0
                print('sum elif: ', sum )
            else:
                return False

            for char in isbn:
                print('lem',len(isbn))
                sum = sum + int(char) * c
                print( 'sum ', sum )
                c -= 1
                print( 'c ', c )
                # continue

            return sum % 11 == 0
        else:
            return False
    else:
        return False















if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print( f"*is isbn valid?: {is_valid('359821507X')}*" )
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')