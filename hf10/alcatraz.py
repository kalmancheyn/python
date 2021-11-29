

def main():
    list_of_cells = [0] * 600
    open_cells = []
    for i in range(len(list_of_cells) + 1):
        for idx, value in enumerate(list_of_cells):
            if (idx + 1) % (i + 1) == 0:
                if list_of_cells[idx] == 0:
                    list_of_cells[idx] = 1
                else:
                    list_of_cells[idx] = 0

    for idx, j in enumerate(list_of_cells):
        if j == 1:
            open_cells.append(idx+1)
    print(open_cells)


if __name__ == "__main__":
    main()