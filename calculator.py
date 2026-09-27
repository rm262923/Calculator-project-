# Simple Calculator Project
# This program asks the user for two numbers and an operation
# then it does the math and shows the answer.
# I used a while loop so the user can do many calculations
# without running the program again and again.

print("===== SIMPLE CALCULATOR =====")

# this variable will keep the loop running
keep_going = True

while keep_going:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # taking input as float so it can handle decimal numbers too
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # checking which operation the user picked
    if choice == "1":
        result = num1 + num2
        print("Answer:", result)

    elif choice == "2":
        result = num1 - num2
        print("Answer:", result)

    elif choice == "3":
        result = num1 * num2
        print("Answer:", result)

    elif choice == "4":
        # we have to be careful, dividing by zero gives an error
        if num2 == 0:
            print("Error! You cannot divide by zero.")
        else:
            result = num1 / num2
            print("Answer:", result)

    else:
        print("Invalid choice, please enter 1, 2, 3 or 4.")

    # asking if the user wants to do another calculation
    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        keep_going = False
        print("Thank you for using the calculator. Bye!")
