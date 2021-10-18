

def main():
    summa = 0
    x = 1111
    i = 0
    number = [int(d) for d in str(x)]
    for n in number:
        if n == number[i - 1]:
            summa += n
        i += 1
    print(summa)


if __name__ == '__main__':
    main()
