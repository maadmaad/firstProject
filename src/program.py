#!/usr/bin/python

#komentarz:
def div():
    for i in (1,101):
        if i % 15 == 0:
            print("{}: FuzzBuzz".format(i))
        elif i % 3 == 0:
            print("{}: Fuzz".format(i))
        elif i % 5 == 0:
            print("{}: Buzz".format(i))

div()

