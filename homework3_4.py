## -*- coding: utf-8 -*-
#Написать функцию в которую можно передать сколько угодно значений и оно
# возводит каждое последующее число в степень предыдущего (первое значение возводим в степень один)

def unlimited(*args): #just bunch of arguments inputted here, for keyworded arguments use **kwargs
    powering=1
    for number in args:
        powering = number**powering
        print powering


unlimited(1,2,3,4,5)