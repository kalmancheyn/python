

def main():
    with open("string1.py", "r") as f, open("string1_clean.py", "w") as to:
        for line in f:
            if not line.startswith("#") and not line.lstrip().startswith("#"):
                to.write(line)


if __name__ == '__main__':
    main()