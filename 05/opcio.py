
def hello(name, repeat = 1, postfix = ""):
    for i in range(repeat):
        print(name + postfix)


def greet(name, greeting ="Hello"):
    print(f"{greeting} {name}!")


def main():
    # greet("Lászlo")
    # greet("Lászlo", greeting="Hola")
    # greet("Lászlo", greeting="Bonjour")
    hello("Laci", repeat=3, postfix="!")
    hello("Laci", 3, "!")


if __name__ == '__main__':
    main()
