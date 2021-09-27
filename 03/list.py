

def main():

    a = [8, 3, 9, 4, 7, 2]
    x = a.pop(0) # x értéke 8 lesz és kiveszi a listából
    print(x)
    a.pop() #kiveszi az utolsó elmet a listából
    print(a)
    a = sorted(a)
    print(a)

if __name__=="__main__":
    main()