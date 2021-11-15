

class Sor:
    def __init__(self):
        self.v1 = []
        self.v2 = []

    def append(self, value):
        self.v1.append(value)

    def popleft(self):
        self.v2 = self.v1[::-1]
        x = self.v2.pop()
        self.v1 = self.v2[::-1]
        return x

    def is_empty(self):
        if len(self.v1) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.v1)

    def __str__(self):
        return str(self.v1)


def main():
    s = Sor()
    s.append(1)
    s.append(2)
    s.append(3)
    print(s)
    print(s.popleft())
    print(s)
    s.append(1)
    print(s)
    print(s.is_empty())
    print(s.size())


if __name__ == "__main__":
    main()