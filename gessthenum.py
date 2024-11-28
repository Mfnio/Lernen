import random
number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("enter guess: "))

    if (guess < number):
        print("Higher")
    elif (guess > number):
        print("Lower")
    else:
        print("you won")        
