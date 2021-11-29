import sys


def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("Kérem számot adjon meg!!!")
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
        except ZeroDivisionError:
            print("Kérem osztónak ne 0-át adjon meg!")
            

if __name__ == "__main__":
    main()