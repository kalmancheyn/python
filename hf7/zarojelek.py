

def isValidParenthese(s):
    str1 = list(s)
    for i in s:
        if i != "(" and i != ")" and i != "{" and i != "}" and i != "[" and i != "]":
            str1.remove(i)
    stack = []
    d = {"(": ")", "{": "}", "[": "]"}
    for i in list(str1):
        if i in d:
            stack.append(i)
        elif d[stack.pop()] != i:
            return False
    return len(stack) == 0


def main():
    print(isValidParenthese("((5+3)*2+1)"))
    print(isValidParenthese("{[(3+1)+2]+}"))
    print(isValidParenthese("(3+{1-1)}"))
    print(isValidParenthese("[1+1]+(2*2)-{3/3}"))
    print(isValidParenthese("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == '__main__':
    main()
