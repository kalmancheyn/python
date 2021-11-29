

def main():
    counter = 0
    with open("corpus.txt", "r") as f:
        for line in f:
            line = line.split(",")
            char_j = line[0].find("j")
            char_s = line[0].find("s")
            char_u = line[0].find("u")
            char_n = line[0].find("n")
            if "j" in line[0] and "s" in line[0] and "u" in line[0] and "n" in line[0] and char_n > char_u > char_s > char_j:
                counter += 1
                print(line[0])


if __name__ == '__main__':
    main()