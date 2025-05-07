totalScore = 0
subjectCount = 0

def Menu():
    print("\nMenu:")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")

def AddScore():
    global totalScore, subjectCount
    subject = input("Enter the subject: ")
    scoreInput = input("Enter the score: ")
    score = float(scoreInput)
    totalScore = totalScore + score
    subjectCount = subjectCount + 1
    print("Score added.")

def CalculateAverage():
    if subjectCount == 0:
        print("No scores to calculate average.")
    else:
        average = totalScore / subjectCount
        print("Average Grade:", average)

while True:
    Menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        AddScore()
    elif choice == "2":
        CalculateAverage()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
