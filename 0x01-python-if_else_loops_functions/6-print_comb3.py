#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        print("{:02d}{:02d}".format(x, y), end=", " if x < 8 or y < 9 else "{:02d}{:02d}\n".format(x, y))
