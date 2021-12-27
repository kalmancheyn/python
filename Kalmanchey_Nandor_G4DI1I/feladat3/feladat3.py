import json
from pprint import pprint


def is_palindrome(x):
    print(x)
    s = str(x)
    if s == s[::-1]:
        return True
    return False


def main():
    with open("primes.json", "r") as f:
        d = json.load(f)
    for k, v in d.items():
        if is_palindrome(v):
            print(v)


if __name__ == "__main__":
    main()