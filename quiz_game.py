print("Welcome to my QUIZ!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Lets play! :)")
score = 0

answer = input("What does CPU stand for? ").lower()

#Question 1
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("You got it wrong!")


#Question 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("You got it wrong!")
    
#Question 3
answer = input("What does PC stand for? ").lower()
if answer == "personal computer":
    print("Correct!")
    score+=1
else:
    print("You got it wrong!")

#Question 4
answer = input("What is the capital of UAE?").lower()
if answer == "AbuDhabi" or "Abu Dhabi`":
    print("Correct!")
    score+=1
else:
    print("You got it wrong!")

print("Good job, you completed the game your score is " + str(score))
print("You got " + str((score / 4)* 100) + "%")