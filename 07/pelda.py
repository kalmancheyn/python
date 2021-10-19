

def main():
    f1 = open("szoveg.txt", "r")
    to = open("szoveg2.txt", "w")

    for line in f1:
        to.write(line)

    to.close()
    f1.close()


if __name__ == '__main__':
    main()