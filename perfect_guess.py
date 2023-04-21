import random
n=random.randint(1,100)


quit='N'
guess=0

while (quit =='N' or quit =='n'):
    num=int(input("Enter your guess between 1 & 100: "))
    guess+=1

    if(num == n):
        print(f"You've made the correct guess in {guess} attempts. The number was {num}.")

        #To check if you've made a highscore or not. If yes, update in highscore.txt
        with open("perfect_guess/highscore.txt", "r") as f:
            highscore = int(f.read())

        if(guess<highscore):
            print("Congratulations!! You've just broken the highest score!")
            print(f"Previous High Score: {highscore}")
            with open("perfect_guess/highscore.txt", "w") as f:
                f.write(str(guess))
        else:
            print(f"High Score: {highscore}")
        break

    elif(num > n):
        print("You've made a wrong guess. The number is SMALLER than your guess.")
        quit= input("Do you want to quit? (y/n)")
    
    else:
        print("You've made a wrong guess. The number is GREATER than your guess.")
        quit= input("Do you want to quit? (y/n)")

if(quit=='Y' or quit=='y'):
    print(f"You lost!! The correct number was {n}")
    



    

