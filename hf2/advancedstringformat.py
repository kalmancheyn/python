

def main():
    print("Battlefield games release after 2010")

    games_info = [("Battlefield 3", 2011), ("Battlefield 4", 2013),
                 ("Battlefield Hardline", 2015), ("Battlefield 1", 2016), ("Battlefield V", 2018)]

    print("{0:25}{1:>25}".format("Title", "Release date"))
    print("-" * 50)

    for elment in games_info:
        print("{0:25}{1:>25}".format(elment[0], elment[1]))
if __name__=="__main__":
    main()