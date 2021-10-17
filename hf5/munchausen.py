

def main():
    for i in range(440000000):
        summa = 0
        number = [int(d) for d in str(i)]
        for digit in number:
            if digit != 0:
                summa += digit ** digit
        if summa == i:
            print(i, "(munchausen)")


if __name__ == '__main__':
    main()
