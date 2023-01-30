#!/usr/bin/python3
# Imports
import matplotlib.pyplot as plt
from random import choice

def trans_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1

def trans_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1

def trans_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1


if __name__ == '__main__':
    transformations = [trans_1, trans_2, trans_3]
    a1 = [0]
    b1 = [0]
    a, b = 0, 0

    for i in range(100000):
        trans = choice(transformations)
        a, b = trans((a, b))
        a1.append(a)
        b1.append(b)

    plt.rc('figure', figsize=(16, 16))
    plt.plot(a1, b1, 'o')
    plt.title('Sierpinski Triangle')
    plt.savefig('sierpinski.png')
    plt.show()