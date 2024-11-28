print("What do you need ")
print("1, for +")
print("2, for -")
print("3, for *")
print("4, for /")

op = int(input("what did you choose "))
if op == 1:
    #code for +
    num1 = input("enter number 1 ")
    num2 = input("enter number 2 ")
    nam1 = int(num1)
    nam2 = int(num2)
    namx = nam1 + nam2
    print("the sum is", namx)
elif op == 2:
    #code for -
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    nam1 = int(num1)
    nam2 = int(num2)
    namx = nam1 - nam2
    print("Your number is", namx)
elif op == 3:
    #code for *
    num1 = input("enter number 1 ")
    num2 = input("enter number 2 ")
    nam1 = int(num1)
    nam2 = int(num2)
    namx = nam1 * nam2
    print("your namber ", namx)
elif op == 4:
    #code for /
    num1 = input("enter number 1 ")
    num2 = input("enter number 2 ")
    nam1 = int(num1)
    nam2 = int(num2)
    namx = nam1 / nam2
    print("your namber ", namx)
else:
    print("invalid data ")
