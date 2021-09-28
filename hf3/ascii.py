

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""".strip()


def main():
    for char in TEXT:
        if ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
            if ord(char) == 121:
                print("a", end="")
            elif ord(char) == 122:
                print("b", end="")
            elif ord(char) == 89:
                print("A", end="")
            elif ord(char) == 90:
                print("B", end="")
            else:
                print(chr(ord(char) + 2), end="")
        else:
            print(chr(ord(char)), end="")


if __name__=="__main__":
    main()