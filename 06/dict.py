

def main():
    d = {}
    d['a'] = 'alfa'
    d['d'] = 'delta'
    d['o'] = 'omega'
    d['g'] = 'gamma'
    # print(d)
    # print(f"d['a'] {d['a']}")
    # print(f"d.get(x) {d.get('x')}")
    # print(f"'a' in d: {'a' in d}")
    # print(f"d.keys(): {d.keys()}")
    # print(f"list(d.keys()): {list(d.keys())}")
    # print(f"list(d.values()): {list(d.values())}")
    # 
    for k in sorted(d.keys()):
        print(k, "->", d[k])

    # for k, v in d.items():
    #     print(k, "->", v)


if __name__ == '__main__':
    main()