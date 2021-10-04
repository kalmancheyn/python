from time import time


def factorization(x):
   print("A",x,"szam faktora:")
   for i in range(2, int(x / 2 + 1)):
       if x % i == 0:
           print(i)


if __name__ == '__main__':
    start = time()
    n = int(input('N: '))
    factorization(n)
    end = time()

    print(end)