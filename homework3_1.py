## -*- coding: utf-8 -*-

# Переписать первое задание используя генераторы списков
# yt понятно где использовать ГС

while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."


def check_input(x):

    if 1<=x<4:
        btw_one_and_four(x)

    elif 4<=x<7:
        btw_four_and_seven(x)4

    elif 7<=x<10:
        btw_seven_and_ten(x)
    else:
        print "Number is out of specified range... Quiting the programm..."

def btw_one_and_four(x):
    s=raw_input("Enter a string: ")
    n=int(raw_input("Enter repetition times: "))
    while n>0:
        print s
        n-=1

def btw_four_and_seven(x):
    m=int(raw_input("Enter Power degree: "))
    print x**m

def btw_seven_and_ten(x):
    count=10
    while count>0:
        x+=1
        count -=1
        print x

check_input(x)