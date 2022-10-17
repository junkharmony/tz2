import random
import time
f = open('output.txt', 'w')


i = 0
a=[]

while i<100000:
    number = random.randint(1, 101)
    a.append(number)
    f.write(str(number))
    f.write(str(' '))
    i = i+1
f.close()

def _max(ar):
    _ma = ar[0]
    for i in ar:
        if i > _ma:
           _ma = i
    return _ma

print('MAX:',_max(a))

def _min(ar):
    _mi = ar[0]
    for i in ar:
        if _mi >i:
            _mi = i
    return _mi

print('MIN:',_min(a))

def _sum(ar):
    k = 0
    for i in ar:
        k +=i
    return k

print('SUM:',_sum(a))

def _mult(ar):
    k = 1
    for i in ar:
        k *=i
    return k

print('MULT:', _mult(a))