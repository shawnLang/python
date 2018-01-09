L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:1])

print(L[1:3])

print(L[-1])

print(L[-3:-1])

T = list(range(100))

print(T)

print(T[::3])


# -*- coding: utf-8 -*-
def trim(s):
    while ' ' == s[:1]:
        print(s[1:])
        s = s[1:]
    while ' ' == s[-1:]:
        print(s[:-1])
        s = s[:-1]
    return s


trim('  sdf sdfsdf  ')
