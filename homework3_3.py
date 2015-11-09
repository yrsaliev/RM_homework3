## -*- coding: utf-8 -*-
#Напишите функцию, которая разбивает введённую строку на слова и выводит по очереди само слова тире ее длина.
string = raw_input("Введите предложение: ")


def analyze_string(string):
    string2= " ".join(string.split()).split(" ") #сперва очищаем от пробелов, потом делим на слова
    print "Длина каждого слова:"
    for word in string2:
        word = unicode(word, "UTF-8")
        print word, "-", len(word)

analyze_string(string)

