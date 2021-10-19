

def sumOfDigits(number):
    total = 0

    while number != 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


def main():
    number = 2 ** 1000
    print(sumOfDigits(number))
    
    
if __name__ == '__main__':
    main()