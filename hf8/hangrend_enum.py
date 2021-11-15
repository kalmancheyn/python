from enum import Enum


class Hangrend(Enum):
    MELY_HGHK = "aáoóuú"
    MAGAS_MGHK = "eéiíöőüű"


def main():
    s = input("Kérem adjon meg egy szót: ")
    mely = False
    magas = False
    for char in s:
        for i in Hangrend.MELY_HGHK.value:
            if i == char:
                mely = True
        for j in Hangrend.MAGAS_MGHK.value:
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
