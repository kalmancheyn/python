

def pages(s: str) -> str:
    values: list[str] = s.split(",")
    li: list[int] = []
    for i in values:
        if len(i) == 1:
            li.append(int(i))
        else:
            for j in i:
                if j == "-":
                    i = i.split("-")
                    for k in range(int(i[0]), int(i[1]) + 1):
                        li.append(k)
    return ','.join([str(number) for number in li])


def main():
    s: str = input()
    print(pages(s))


if __name__ == "__main__":
    main()