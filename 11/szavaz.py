import requests
import time
import random as r


def sleep(fix=5, plus=5):
    """Sleep for some randomized time.

    Time will be a real value between fix and fix+plus."""
    sec = fix + r.uniform(0, plus)
    time.sleep(sec)
    return sec


def main():
    url = "https://divany.hu/offline/2016/03/07/dontsuk_el_meno_vagy_ciki_az_ovtaska/?p=&meno=1&posztbol=1"
    for i in range(10):
        r = requests.get(url)
        sleep()
        print('.', end="", flush=True)
    print()


if __name__ == "__main__":
    main()