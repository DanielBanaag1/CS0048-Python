def Temperature_converter():
    while True:
        print("\n ====Menu==== ")
        print("1. Celsius to Fahrenheit ")
        print("2. Fahrenheit to Celsius ")
        print("3. Exit ")
        choice = int(input("Please Enter your choice: "))

        if choice == 1:
            Cel = float(input("Enter temperature in celsius: "))
            Fah = (Cel * 9 / 5) + 32
            print("Temperature in Fahrenheit: ", Fah)

        elif choice == 2:
            Fah = float(input("Enter temperature in Fahrenheit"))
            Cel = (Fah - 32) * 5 / 9
            print("Temperature in Celsius", Cel)
        
        elif choice == 3:
            print("Goodbye! thank u for using temperature converter! ")
            break

        else: 
            print("Invalid choice! ")

Temperature_converter()
    
