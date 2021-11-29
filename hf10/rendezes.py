

def my_func1(t):
    return t[-1]


def my_func2(s):
    return int(s.split(":")[0])


def my_func3(li):
    return li[1]


def main():
    data = [
        (1, 'Albany', 'NY', 162692),
        (3, 'Allegany', 'NY', 11986),
        (121, 'Wyoming', 'NY', 8722),
        (123, 'Yates', 'NY', 5094)
    ]
    print(sorted(data, key=my_func1))
    print(sorted(data, key=lambda t: t[-1]))

    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(lst, key=my_func2, reverse=True))
    print(sorted(lst, key=lambda s: int(s.split(":")[0]), reverse=True))

    li = [[2, 6], [1, 3], [5, 4]]
    print(sorted(li, key=my_func3))
    print(sorted(li, key=lambda l: l[1]))


if __name__ == "__main__":
    main()