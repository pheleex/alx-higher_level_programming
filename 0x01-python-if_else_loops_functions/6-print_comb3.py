#!/usr/bin/python3
for i in range(10):
    for num in range(10):
        if (num > i and i != 8):
            print("{}{}".format(i, num), end=", ")
        elif (i == 8 and num == 9):
            print("{}{}".format(i, num))
            break
