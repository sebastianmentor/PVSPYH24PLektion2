from math import sqrt

name = input('Skriv ditt namn: ')

print(sqrt(9))
print(name.upper())
print(name)
print(str.upper(name))

skriv_ut_i_terminalen = print

skriv_ut_i_terminalen('Hejsan hoppsan!!!')

with open('hej.txt','w') as f:
    print(name.__str__(), file=f)

