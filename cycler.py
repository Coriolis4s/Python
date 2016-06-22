from itertools import cycle
from time import sleep
from sys import stdout

def cycler():
    x = ['|','/','+','|','+']
    p = cycle(x)
    while True:
        stdout.write(('\b%s' %(p.next())))

if __name__ == "__main__":
        cycler()
