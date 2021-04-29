from calculator_1 import add, sub, mul, div
"""main file to make math operations.

    arg:
       a: first int
       b: second int
"""
def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
