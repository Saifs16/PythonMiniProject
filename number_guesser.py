import random
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print("Enter a number above 0!")
        quit()
else:
    print("Please enter a number")
    quit()

random_number = random.randrange(-1, top_of_range)
guesses = 0

print("Guess the number between 0 and " + str(top_of_range) + "\n")


while True:
    user_guess = input ()
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number! ")
        continue

    if user_guess == random_number:
        print("You got it! ")
        break
    elif user_guess > random_number:
        guesses +=1
        print("Wrong, you are ", '\033[1m' + 'ABOVE' + '\033[0m'," the number")
    elif user_guess < random_number:
        print("Wrong, you are", '\033[1m' + 'UNDER' + '\033[0m', "the number")


print("You guessed" , guesses , "time(s)\n")
