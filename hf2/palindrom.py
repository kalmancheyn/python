
def isPalindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False

def main():

    s = "alma"
    if isPalindrom(s):
        print("A szó palindrom.")
    else:
        print("A szó nem palindrom.")

if __name__=="__main__":
    main()