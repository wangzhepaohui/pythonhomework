import math


def calnumbers():
    numbers = []
    for i in range(-100, 1000000):
        a = math.sqrt(i + 100)
        b = math.sqrt(i + 100 + 168)
        if (int(a) == a) & (int(b) == b):
            numbers.append(i)
    return numbers


def main():
    print("There is not only one such number, these numbers are:",calnumbers())


if __name__ == "__main__":
    main()
