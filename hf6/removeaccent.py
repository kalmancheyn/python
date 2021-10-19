TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
""".strip()


def removeAccentWithReplace(s):
    s = s.replace("á", "a").replace("é", "e").replace("í", "i") \
        .replace("ó", "o").replace("ö", "o").replace("ő", "o") \
        .replace("ú", "u").replace("ü", "u").replace("ű", "u") \
        .replace("Á", "A").replace("É", "E").replace("Í", "I") \
        .replace("Ó", "O").replace("Ö", "O").replace("Ő", "O") \
        .replace("Ú", "U").replace("Ü", "U").replace("Ű", "U")

    return s


def removeAccentWithDict(s):
    d = {'á': 'a', 'Á': 'A', 'é': 'e', 'É': 'E', 'í': 'i', 'Í': 'I', 'ó': 'o', 'Ó': 'O', 'ö': 'o', 'Ö': 'O', 'ő': 'o',
         'Ő': 'O', 'ú': 'u', 'Ú': 'U', 'ü': 'u', 'Ü': 'U', 'ű': 'u', 'Ű': 'U'}

    for char in s:
        for k, v in d.items():
            if k == char:
                s = s.replace(char, v)
    return s


def main():
    print(f"With Replace:\n{removeAccentWithReplace(TEXT)}")
    print('*' * 100)
    print(f"With dict:\n{removeAccentWithDict(TEXT)}")


if __name__ == '__main__':
    main()
