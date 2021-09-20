

import sys

def main():

    if len(sys.argv) != 3:
        print("Kérem adjon meg 2 számot parancsori argumentumként(szóközzel elválasztva)!")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print("A két szám összege: {0} + {1} = {2}".format(x, y, x + y))


if __name__=="__main__":
    main()