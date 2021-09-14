

PI = 3.14159

def hello(name, color, what):
    #geza kek az eg!
    #C:
    #print("%s, %s az %s!\n", name, color,what)
    #v1:
    #print("{0}, {1} az {2}! Ki? {0}".format(name, color, what))
    #v2:
    #print("{}, {} az {}!".format(name, color, what))
    #v3:
    #print("{nev}, {szin} az {obj}!".format(nev=name, szin=color, obj=what))
    #v4:
    #print(f"1 + 1 = {1 + 1}")
    print(f"{name.capitalize()}, {color} az {what}!")


def main():
    hello("geza", "kek", "eg")
    print("-" * 30)
    hello("Julcsi", "piros", "auto")


if __name__=="__main__":
    main()