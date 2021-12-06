import json


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    prims = []
    for n in range(10000000+1):
        if is_prime(n):
            prims.append(n)
    print(prims)

    with open('prims.json', 'w') as f:
        json.dump(prims, f)


if __name__ == "__main__":
    main()