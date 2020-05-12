import math


def trailingzeros(n):
    total = 0
    while (n):
        n = int(n / 5)
        total += n
    return total


def main():
    n = eval(input("Please enter the number to be calculated:"))
    if (n >= 0):
        print('{}! = {},The number of zeros is {}'.format(n, math.factorial(n), trailingzeros(5)))
    else:
        print("Erros,Please enter a natural number")


if __name__ == "__main__":
    main()
