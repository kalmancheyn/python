


def main():
    # kosar = ["alma", "ananasz", "banan", "alma", "narancs", "banan"]
    # gyumolycs = set(kosar)
    # print(gyumolycs)
    # print("kiwi" in gyumolycs)
    # print("narancs" in gyumolycs)
    # li = list(gyumolycs)
    # print(sorted(li))
    #print(sorted(set([5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5])))
    a = ["alma", "banan", "citrom"]
    a = set(a)
    print(f"a: {a}")
    b = set()
    b.add("banan")
    b.add("narancs")
    print(f"b: {b}")
    print(f"union: {a.union(b)}")
    print(f"intersevtion: {a.intersection(b)}")
    print(f"difference: {a.difference(b)}")
    print(b.remove("narancs"))



if __name__ == '__main__':
    main()
