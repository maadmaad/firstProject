#!/usr/bin/python

def div():
    for i in (1,101):
        if i % 15:
            print("{}: FuzzBuzz".format(i))
        elif i % 3:
            print("{}: Fuzz".format(i))
        elif i % 5:
            print("{}: Buzz".format(i))

div()

