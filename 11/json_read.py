from pprint import pprint
import json


def main():
    fname = "person.json"
    f = open(fname)

    d = json.load(f)
    pprint(d)

    f.close()


if __name__ == "__main__":
    main()