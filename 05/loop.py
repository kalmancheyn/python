
def loop(n, debug=False):
    if debug:
        print("#ciklus kezdete")
    for i in range(1, n + 1):
        print(f"{i} ", end="")
    print()
    if debug:
        print("#ciklus vége")


def main():
    # loop(10)
    loop(10, True)


if __name__ == '__main__':
    main()
