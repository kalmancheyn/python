

def main():
    parts = []
    for i in range(1, 101):
        parts.append(str(i))

    res = "".join(parts)
    list(res)
    sum = 0
    for i in res:
        sum += int(i)
    print(sum)


if __name__ == "__main__":
    main()