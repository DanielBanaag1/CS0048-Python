def ToDoList():
    t1 = ""
    t2 = ""
    t3 = ""

    while True:
        print("\n ==== asdasd ==== ")
        print("1. Add task ")
        print("2. remove task ")
        print("3. View task ")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            t = input("Enter task: ")
            if t1 == "":
                t1 = t
                print("Added! ")
            
            elif t2 == "":
                t2 = t
                print("Added! ")

            elif t3 == "":
                t3 = t
                print("Added! ")
            
            else: 
                print("Task is Full!! ")
            

        elif choice == 2:
            t = input("Remove task: ")

            if t == t1:
                t1 = ""
                print("removed! ")
            
            elif t == t2:
                t2 = ""
                print("removed! ")

            elif t == t3:
                t3 = ""
                print("removed! ")
            
            else: 
                print("Task not found! ")

        elif choice == 3:
            if t1 != "":
                print("-", t1)

            if t2 != "":
                print("-", t2)

            if t3 != "":
                print("-", t3)
            
            if t1 == "":
                if t2 == "":
                    if t3 == "":
                        print("No task! ")

        elif choice == 4:
            break

        else: 
            print("Invalid CHoice!!! ")
ToDoList()


