
def summa() -> int:
    sum: int = 0
    for i in range(0, 1_000_000):
        bin_num: str = bin(i)
        i = str(i)
        if i == i[::-1] and bin_num[2:] == bin_num[:1:-1] and bin_num[2:3] != 0:
            sum += int(i)
    return sum


def main():
    print(summa())


if __name__ == "__main__":
    main()