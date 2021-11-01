

def main():
    c = 0
    while c < 1000:
        a = 0
        b = 0
        c = 0
        for i in range(1000):
            a += 1
            for j in range(1000):
                b += 1
                for k in range(1000):
                    c += 1
            if a < b//100 < c//100000:
                print(f"{a}, {b}, {c}")

if __name__ == '__main__':
    main()