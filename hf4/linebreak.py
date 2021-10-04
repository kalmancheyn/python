import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO//10):
        for j in range(UPTO//10):
            print(r.randint(0, 9), end="")
        print()

    print()


if __name__ == "__main__":
    main()