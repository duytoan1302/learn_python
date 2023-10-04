import random
number = random.randint(1,20)
guess = int(input("I am thinking about one number 1 to 20.What the number I thinking."))
while guess != number:
    if guess < number: 
        print("The number you guess is so small...")
    else:
        print("The number you guess is so big...")
    guess = int(input("Please guess again..."))
print("Yeah you is win the game.")
