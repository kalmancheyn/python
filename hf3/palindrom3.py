

def isPalindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])


def main():

    s = "gorog"
    if isPalindrome(s):
        print("A szó palindrom.")
    else:
        print("A szó nem palindrom.")

if __name__=="__main__":
    main()