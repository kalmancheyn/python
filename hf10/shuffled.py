import random


def shuffled(li):
    shuffled_li = li.copy()
    random.shuffle(shuffled_li)
    return shuffled_li


def main():
    li = [2, 4, 6, 7, 3]
    print(shuffled(li)[-1])


if __name__ == "__main__":
    main()