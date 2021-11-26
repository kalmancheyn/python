import random


def my_shuffle(li: list[int]) -> list[int]:
    copy = li[:]    #li.copy()
    random.shuffle(copy)
    return copy


def main():
    print(random.random())
    print(random.randint(1, 3))
    li = [3, 4, 6, 7, 8]
    print(random.shuffle(li))
    print(random.choice(li))
    print(my_shuffle(li))


if __name__ == "__main__":
    main()
