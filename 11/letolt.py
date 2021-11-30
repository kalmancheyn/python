import os
import requests


def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg"
    cmd = f"curl {url}"
    os.system(cmd)


if __name__ == "__main__":
    main()