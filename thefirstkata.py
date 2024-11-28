def get_int():
    numbers = []  # Initialize an empty list to store numbers
    numbers.append(int(input("Enter a number: ")))
    return numbers

def calculate_sum_of_squares(number):
    x = number // 100
    xx = (number // 10) % 10
    xxx = number % 10     

    z = x * x
    zz = xx * xx
    zzz = xxx * xxx 
    c = z + zz + zzz
    return c

numbers = get_int()  # Get the user's number
result = calculate_sum_of_squares(numbers[0])  # Calculate the sum of squares
print("Result:", result)


"""
My code with my brain
numbers = []
def get_int():
    numbers.append(int(input("what's the number ")))
    print("the numbers are", c)
def lol():

    x = numbers[0] // 100
    xx = (numbers[0] // 10) % 10
    xxx = numbers[0] % 10     

    z = x * x
    zz = xx * xx
    zzz = xxx * xxx 
    c = z + zz + zzz
    return c
lol()
get_int()
"""
