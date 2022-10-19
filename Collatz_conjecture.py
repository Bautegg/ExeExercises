def steps(number):
        count = 0
        if number <= 0:
            raise ValueError( "Only positive integers are allowed" )
        while number > 1:
            count +=1
            # print(count, number)
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number +1

        return count





if __name__=='__main__':
    print(f'steps: {steps(1)}')
    # print(add_prefix_un(input("vEnter number: ")))
    print(f'steps: {steps(16)}')
