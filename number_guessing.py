import random


print("Hi! Welcome to the number guessing game.\nYou have 5 chances to guess the number.")

low = int(input("Enter lower bound(eg. 1): "))
upper = int(input("Enter upper bound(eg. 10): "))

print(f"You have 5 chances to guess the number between {low} and {upper}.")

num = random.randint(low, upper)
chances = 5
guess_count = 0

while guess_count < chances:
    guess_count += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print("Congrats! You guessed correctly.")
        break
    elif guess < num:
        print("Too low!")
    else:
        print("Too high!")

if guess_count == chances and guess != num:
    print("Sorry, you ran out of chances.")
    print("The number was:", num)
