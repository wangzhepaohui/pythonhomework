def comparenumbers():
    l = list(map(int, input('Please enter three numbers, separated by spaces').split()))
    list.sort(l)
    print(l)


def main():
    comparenumbers()


if __name__ == "__main__":
    main()
