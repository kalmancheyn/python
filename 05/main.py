

def duplaz():
    pass


def main():
    li = ["alfa", "beta", "gamma"]

    print(list(enumerate(li)))

    for index, e in enumerate(li, start=1):
        print(index, "->", e)


if __name__ == '__main__':
    main()
