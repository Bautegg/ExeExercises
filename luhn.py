class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
            string_card = self.card_num.replace(" ","")

            if string_card.isnumeric() and string_card != '0':
                lista_card = [int(x) for x in string_card]
                print(lista_card)
                for i in range(-2,-len(lista_card)-1,-2):
                    print(f'i= {i}')
                    co_druga = lista_card[i] * 2
                    print(co_druga)
                    if co_druga > 9:
                        co_druga -= 9
                        print( co_druga )
                    lista_card[i] = co_druga
                print(lista_card)
                return sum(lista_card) % 10 == 0
            else:
                return False


if __name__ == '__main__':
    # print(add_prefix_un(input("vEnter number: ")))
    moja_karta = Luhn(card_num = '   0    ')
    moja_karta.valid()
    print( f'Mój numer karty?: {moja_karta.valid()}' )