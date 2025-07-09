def main():
    x = int(input("What's x? "))
    if fun(x):
        print("is Even")
    else:
        print("is not Even")


def fun(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False


main()
