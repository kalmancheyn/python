

def main():
    result = sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0])
    print(result)


if __name__ == '__main__':
    main()
