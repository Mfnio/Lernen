def main():
    n = int(input("How many stars do you want in rows? "))
    staring(n)


def staring(i):
    z = 1
    while z <= i:
        print("*" * z)
        z = z + 1
        
        
main()

