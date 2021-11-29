import sys


def cat(fname):
    try:
        f = open(fname, 'r')
        text = f.read()
        print('---', fname)
        print(text)
        f.close()
    except FileNotFoundError as e:
        print(e)
        print("Warning!")


if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        cat(arg)