

def isPalindrome(s):
    return s == s[::-1]


def main():

    s = "gorog"
    if isPalindrome(s):
        print("A szó palindrom.")
    else:
        print("A szó nem palindrom.")

if __name__=="__main__":
    main()