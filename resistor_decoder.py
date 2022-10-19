def value(colors):
    slownik = dict(black='0', brown='1', red= '2', orange= '3', yellow= '4', green= '5', blue= '6', violet= '7', grey= '8', white= '9')
    # a = slownik[colors[0]]
    # b = slownik[colors[1]]
    # val = ''.join([a,b])
    return int(''.join([slownik[colors[0]],slownik[colors[1]]]))


if __name__=='__main__':
    # print(f"steps: {create_inventory([('coal',12), ('iron',5), ('supply',False)])}")
    print( f"*is isbn valid?: {value(['black','green'])}*" )
    # print(add_prefix_un(input("vEnter number: ")))
    # print(f'steps: {steps(16)}')