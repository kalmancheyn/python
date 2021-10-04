

def main():
    height = int(input("Kérem adjon meg egy páratlan számot: "))
    if height % 2 == 0:
        while height % 2 == 0:
            height = int(input("Kérem páratlan számot adjon meg! "))
    for i in range(1, (height + 1) // 2 + 1):  # from row 1 to 5
        for j in range((height + 1) // 2 - i):
            print(" ", end="")
        for k in range((i * 2) - 1):
            print("*", end="")
        print()

    for i in range((height + 1) // 2 + 1, height + 1):  # from row 6 to 9
        for j in range(i - (height + 1) // 2):
            print(" ", end="")
        for k in range((height + 1 - i) * 2 - 1):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()