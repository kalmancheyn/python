

# class EmptyClass:
#     pass


class MyClass:
    def hello(self):
        return "hello obj"


def main():
    #empty = EmptyClass()
    obj = MyClass()
    print(obj.hello())


if __name__ == "__main__":
    main()
