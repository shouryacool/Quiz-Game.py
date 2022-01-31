print("Welcome To My Computer Quiz!")
playing = input("Do You Want To Play? (y/n):\n")
if playing.lower() != "y":
    quit()
else:
    print("Okay! Let's play")
score=0    

    # 1st Question
answer = input("What Does CPU stand for?\n").lower()
if answer == "Centeral Processing Unit":
    print("Correct!")
    score+=1
else:
    print("Sorry,Incorrect")
    # 2nd Question
answer = input("What Does GPU stand for?\n").lower()
if answer == "Graphic Processing Unit":
    print("Correct!")
    score+=1
else:
    print("Sorry,Incorrect")

    # 3rd Question
answer = input("What Does RAM stand for?\n").lower()
if answer == "Random Access Memory":
    print("Correct!")
    score+=1
else:
    print("Sorry,Incorrect")

    # 4th Question
answer = input("What Does PSU stand for?\n").lower()
if answer == "Power Supply Unit":
    print("Correct!")
    score+=1
else:
    print("Sorry,Incorrect")
    
print("You Got" + str(score) + "Questions Correct!")

print("You Got" + str((score/4)*100) + "%.")