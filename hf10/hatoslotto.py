import sys
from itertools import combinations


def mult_tuple(t):
    mult = 1
    for value in t:
        mult *= value
    return mult


def main():
    for comb in combinations(range(1, 46), 6):
        if sum(comb) == 90 and mult_tuple(comb) == 996300:
            print(comb)
            sys.exit(0)


if __name__ == "__main__":
    main()