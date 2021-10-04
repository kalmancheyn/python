
MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def main():
    s = input("Kérem adjon meg egy szót: ")
    mely = False
    magas = False
    for char in s:
        for i in MELY_MGHK:
            if i == char:
                mely = True
        for j in MAGAS_MGHK:
            if j == char:
                magas = True

    if magas and mely:
        print("vegyes")
    elif magas:
        print("magas")
    elif mely:
        print("mély")
    else:
        print("semmilyen")


if __name__ == "__main__":
    main()
