import sys


def main():
    if len(sys.argv) == 2:
        with open("data.csv", "r") as f:
            for line in f:
                line = line.split(";")
                ssn = line[-2]
                ssn = list(ssn)
                if sys.argv[1] == ssn[0]:
                    print(f"{line[2]}, {line[-2]}")
    else:
        print("Hibás paraméterezés! Csak egy számjegyet kell megadni!")


if __name__ == '__main__':
    main()