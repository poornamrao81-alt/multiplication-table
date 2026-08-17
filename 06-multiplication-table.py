print("===== MULTIPLICATION TABLE GENERATOR =====")

while True:
    try:
        number = int(input("\nEnter the number for the table: "))
        start = int(input("Enter starting value: "))
        end = int(input("Enter ending value: "))

        if start > end:
            print("Starting value should be smaller than ending value.")
            continue

        print("\nMultiplication Table of", number)
        print("-----------------------------")

        for i in range(start, end + 1):
            result = number * i
            print(number, "x", i, "=", result)

        again = input("\nDo you want to generate another table? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the program!")
            break

    except ValueError:
        print("Please enter numbers only.")