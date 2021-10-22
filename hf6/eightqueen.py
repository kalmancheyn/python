def boardPrint(l):
    board = [["+", "---", "---", "---", "---", "---", "---", "---", "---", "+"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["|", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", "|"],
             ["+", "---", "---", "---", "---", "---", "---", "---", "---", "+"]]
    f = 1
    for i in l:
        board[(i - 8) * -1][f] = ' Q '
        f += 1
    for j in range(10):
        for k in range(10):
            print(board[j][k], end="")
        print()
    return


def main():
    li1 = [7, 3, 0, 2, 5, 1, 6, 4]
    li2 = [0, 4, 7, 5, 2, 6, 1, 3]
    boardPrint(li1)
    print("*" * 40)
    boardPrint(li2)


if __name__ == '__main__':
    main()