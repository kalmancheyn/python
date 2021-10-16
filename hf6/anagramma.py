

def normalize(s):
    return s.lower().replace(" ","")


def anagramma1(s1, s2):
    s1 = list(normalize(s1))
    s2 = list(normalize(s2))
    return sorted(s1) == sorted(s2)


def anagramma2(s1, s2):
    s1 = list(normalize(s1))
    s2 = list(normalize(s2))
    d1 = {}
    d2 = {}
    for word in s1:
        if word in d1.keys():
            d1[word] += 1
        else:
            d1[word] = 1

    for word in s2:
        if word in d2.keys():
            d2[word] += 1
        else:
            d2[word] = 1

    return d1 == d2


def main():
    s1 = "Clint Eastwood"
    s2 = "Old west action"
    print(anagramma1(s1,s2))
    print(anagramma2(s1,s2))


if __name__ == "__main__":
    main()