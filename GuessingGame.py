import random

def GuessingGame():
    while True:
        print("\n ==== Menu ==== ")
        print("1. Play the guessing game ")
        print("2. Exit ")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = random.randint(1,100)
            attempts = 0
            guessed = False
            while guessed == False:
                guess = int(input("Enter the number between 1-100: "))
                attempts = attempts + 1
                if guess > num:
                    print("Number too high! ")
                elif guess < num:
                    print("Number too low! ")

                else:
                    print("Congratulations! you won in ", attempts, "attempts")
                    guessed = True
                
        elif choice == 2:
            print("Thank you for using the game :) ")
            break

        else:
            print("Invalid choice! ")
GuessingGame()

