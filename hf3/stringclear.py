

def clearString(s):
    s = "".join(s.split())
    return s

def main():
    s = "     jghjg   \n\n   hgk\tjhkj"
    print(clearString(s))

if __name__=="__main__":
    main()