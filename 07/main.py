

def main():
    f = open("szoveg.txt", "r")

    # content = f.read()
    # print("'" + content + "'")

    # sorok = f.readlines()
    # print(sorok)

    sorok = f.read().splitlines()
    print(sorok)

    # for line in f:
    #     line = line.rstrip("\n")
    #     if line.endswith("."):
    #         print(line)

    f.close()


if __name__ == '__main__':
    main()
