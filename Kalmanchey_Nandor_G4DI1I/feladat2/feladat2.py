import json


def main():
    i = 0
    data = []
    with open("primes.php", "r") as f:
        for line in f:
            if i != 0:
                line = line.split(">")
                line = line[1].split(",")
                data.append(line[0])
            i += 1
    print("-> primes.php beolvasva")
    data.remove("")
    d = {}
    d["description"] = "list of prime numbers"
    d["data"] = data
    with open("primes.json", "w") as f:
        json.dump(d, f)
    print("-> primes.json létrehozva")


if __name__ == "__main__":
    main()