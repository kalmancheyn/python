#A billentyűzetről bekért szöveget nagybetűvel írja ki.


def main():
    s = input("Szöveg: ")
    print("A bekért szöveg átalakítva: " + s.upper())

if __name__=="__main__":
    main()