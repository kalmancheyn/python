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
    d = {}
    d['á'] = 'a'; d['Á'] = 'A'; d['é'] = 'e'; d['É'] = 'E'
    d['í'] = 'i'; d['Í'] = 'I'; d['ó'] = 'o'; d['Ó'] = 'O'
    d['ö'] = 'o'; d['Ö'] = 'O'; d['ő'] = 'o'; d['Ő'] = 'O'
    d['ú'] = 'u'; d['Ú'] = 'U'; d['ü'] = 'u'; d['Ü'] = 'U'
    d['ű'] = 'u'; d['Ű'] = 'U'

    for k,v in d.items():
        print(k, " -> ", v)


def main():
    print(f"With Replace:\n{removeAccentWithReplace(TEXT)}")
    print(removeAccentWithDict(TEXT))


if __name__ == '__main__':
    main()
