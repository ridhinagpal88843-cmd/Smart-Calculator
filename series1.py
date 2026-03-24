import datetime;
print("Welcome to Smart Calculator ");

history = [];  # to store calculation history

while True:
    print("\n========== MENU ==========");
    print("1. Add");
    print("2. Subtract");
    print("3. Multiply");
    print("4. Divide");
    print("5. Show History ");
    print("6. Save History ");
    print("7. Exit");
    print("==========================");

    choice = input("Enter your choice (1-7): ");

    if choice == '7':
        print("Thank You!!!");
        break;

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "));
            num2 = float(input("Enter second number: "));

            if choice == '1':
                result = num1 + num2;
                operation = "+";

            elif choice == '2':
                result = num1 - num2;
                operation = "-";

            elif choice == '3':
                result = num1 * num2;
                operation = "*";

            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!");
                    continue;
                result = num1 / num2;
                operation = "/";

            output = f"{num1} {operation} {num2} = {result}";
            print("Result:", output);

            history.append(output);

        except ValueError:
            print("Invalid input! Please enter numbers only.");

    elif choice == '5':
        print("\nCalculation History:");
        if not history:
            print("No calculations yet.");
        else:
            for item in history:
                print(item);

    elif choice == '6':
        with open("history.txt", "w") as file:
            for item in history:
                file.write(item + "\n");
        print("History saved to 'history.txt'");

    else:
        print("Invalid choice! Try again.");