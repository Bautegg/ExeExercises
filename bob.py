def response(hey_bob):
    if (hey_bob.isspace()==True or hey_bob == ""):
        return 'Fine. Be that way!'
    else:
        hey_bob = hey_bob.strip()

        if(hey_bob.endswith('?') == True and (hey_bob.isupper()) == True):
            return "Calm down, I know what I'm doing!"
        elif(hey_bob.isupper() == True):
            return 'Whoa, chill out!'
        elif(hey_bob.endswith('?') == True):
            return 'Sure.'
        else:
            return 'Whatever.'


if __name__ == '__main__':
    # print(add_prefix_un(input("Enter number: ")))
    print( f"Bob s answer: {response('')}" )
