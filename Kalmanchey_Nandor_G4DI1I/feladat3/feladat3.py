
def pascalTriangle(n):
    row = [1]
    y = [0]
    for i in range(n):
        row = [left+right for left, right in zip(row+y, y+row)]
    return row


def main():

    index = -2
    while index != -1:
        index = int(input("A sor indexe (kilépés: 0): "))
        index -= 1
        if index == -1:
            break
        x = pascalTriangle(index)
        for i in x:
            print(f"{i} ", end="")
        print()

    print("bye")


if __name__ == "__main__":
    main()