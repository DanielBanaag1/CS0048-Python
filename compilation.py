import random

# === Calculator ===
def calculator():
    while True:
        print("\n==== Calculator Menu ====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back to Main Menu")
        choice = int(input("Please Enter your choice: "))

        if choice == 1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", num1 + num2)

        elif choice == 2:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", num1 - num2)

        elif choice == 3:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", num1 * num2)

        elif choice == 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Cannot divide by 0")
            else:
                print("Result:", num1 / num2)

        elif choice == 5:
            break
        else:
            print("Invalid Choice!")

# === Temperature Converter ===
def temperatureConverter():
    while True:
        print("\n==== Temperature Converter Menu ====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Back to Main Menu")
        choice = int(input("Please Enter your choice: "))

        if choice == 1:
            cel = float(input("Enter temperature in Celsius: "))
            fah = (cel * 9 / 5) + 32
            print("Temperature in Fahrenheit:", fah)

        elif choice == 2:
            fah = float(input("Enter temperature in Fahrenheit: "))
            cel = (fah - 32) * 5 / 9
            print("Temperature in Celsius:", cel)

        elif choice == 3:
            break
        else:
            print("Invalid Choice!")

# === To-Do List ===
def toDoList():
    t1 = ""
    t2 = ""
    t3 = ""

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Back to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            if t1 == "":
                t1 = task
                print("Added!")
            elif t2 == "":
                t2 = task
                print("Added!")
            elif t3 == "":
                t3 = task
                print("Added!")
            else:
                print("Task list is full!")

        elif choice == 2:
            task = input("Enter task to remove: ")
            if task == t1:
                t1 = ""
                print("Removed!")
            elif task == t2:
                t2 = ""
                print("Removed!")
            elif task == t3:
                t3 = ""
                print("Removed!")
            else:
                print("Task not found!")

        elif choice == 3:
            if t1 != "":
                print("-", t1)
            if t2 != "":
                print("-", t2)
            if t3 != "":
                print("-", t3)
            if t1 == "" and t2 == "" and t3 == "":
                print("No tasks!")

        elif choice == 4:
            break
        else:
            print("Invalid Choice!")

# === Guessing Game ===
def guessingGame():
    while True:
        print("\n==== Guessing Game Menu ====")
        print("1. Play")
        print("2. Back to Main Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            number = random.randint(1, 100)
            attempts = 0
            guessed = False
            while not guessed:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts = attempts + 1
                if guess > number:
                    print("Too high!")
                elif guess < number:
                    print("Too low!")
                else:
                    print("Congratulations! You guessed in", attempts, "attempts.")
                    guessed = True

        elif choice == 2:
            break
        else:
            print("Invalid Choice!")

# === Student Grade Calculator ===
totalScore = 0
subjectCount = 0

def showGradeMenu():
    print("\n==== Grade Calculator Menu ====")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Back to Main Menu")

def gradeCalculator():
    global totalScore, subjectCount
    while True:
        showGradeMenu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            subject = input("Enter the subject: ")
            score = float(input("Enter the score: "))
            totalScore = totalScore + score
            subjectCount = subjectCount + 1
            print("Score added.")
        elif choice == "2":
            if subjectCount == 0:
                print("No scores to calculate average.")
            else:
                average = totalScore / subjectCount
                print("Average Grade:", average)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

# === Main Menu ===
def mainMenu():
    while True:
        print("\n==== Main Menu ====")
        print("1. Calculator")
        print("2. Temperature Converter")
        print("3. To-Do List")
        print("4. Guessing Game")
        print("5. Student Grade Calculator")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            calculator()
        elif choice == 2:
            temperatureConverter()
        elif choice == 3:
            toDoList()
        elif choice == 4:
            guessingGame()
        elif choice == 5:
            gradeCalculator()
        elif choice == 6:
            print("Goodbye! Program ended.")
            break
        else:
            print("Invalid choice!")

# Run the program
mainMenu()
