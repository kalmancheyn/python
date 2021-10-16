

def isMedian(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2 ]) / 2

def main():
    numbers = [3, 6, 20, 99, 10, 15]
    numbers = sorted(numbers)
    print(isMedian(numbers))


if __name__ == '__main__':
    main()
