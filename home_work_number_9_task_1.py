# -*- coding: utf-8 -*-
def func1():
    my_file = open('snake.txt', 'w')
    my_file.write("Hello file world!")
    my_file.close()
func1()

def func2():
    files = open('snake.txt', 'r')
    for line in files:
        print(line)

func2()