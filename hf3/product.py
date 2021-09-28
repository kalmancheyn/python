

def product(li):
    p = 1
    for value in li:
        p *= value
    return p


def main():
    numbers = [1, 2, 3, 4, 5]
    print(product(numbers))


if __name__=="__main__":
    main()
