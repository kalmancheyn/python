

def main():
    f = open("out.txt", "w")

    print("aaaa", file=f)
    print("bbbb", file=f)

    f.write("cc\n")
    f.write("dd\n")

    f.close()


if __name__ == '__main__':
    main()