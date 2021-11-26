
def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome_and_is_prim(x: int) -> int:
    while True:
        s: str = str(x)
        if s == s[::-1] and is_prime(x):
            return x
        x += 1


def main():
    n1: int = int(input())
    print(is_palindrome_and_is_prim(n1))


if __name__ == "__main__":
    main()
