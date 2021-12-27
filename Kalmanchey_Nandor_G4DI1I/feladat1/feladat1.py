

def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    data = []
    k = 0
    line = list(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            data[i] += list(line[i])
    print(data)
    f.close()


if __name__ == "__main__":
    main()