

def negyzetosszeg():
    summa = 0
    for i in range(11):
        summa = summa + (i*i)
    return summa


def osszegnegyzet():
    summa = 0
    for i in range(11):
        summa = summa + i
    return summa * summa


def main():
    x = negyzetosszeg()
    y = osszegnegyzet()
    print(y-x)


if __name__ == "__main__":
    main()