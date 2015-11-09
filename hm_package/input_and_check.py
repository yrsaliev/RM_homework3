## -*- coding: utf-8 -*-

# Переписать первое задание используя генераторы списков
# yt понятно где использовать ГС

import onetofour, fourtoseven, sevenandten

while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."


def check_input(x):

    if 1<=x<4:
        onetofour.btw_one_and_four(x)

    elif 4<=x<7:
        fourtoseven.btw_four_and_seven(x)

    elif 7<=x<10:
        sevenandten.btw_seven_and_ten(x)
    else:
        print "Number is out of specified range... Quiting the programm..."


check_input(x)
