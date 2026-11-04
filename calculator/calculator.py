def calc(a , op , b):
    if op == "+" :
        return  a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op =="/":
        if b ==0:
            return "Error: Division by zero is not allowed!"
        return a /b
    else:
       "Error: Invalid operator!"
#
while True:
    user_input = input(
        "\nEnter the first number (or type 'q' to exit): "
    ).strip()
    if user_input.lower() == "q":
        print("Exiting program. Goodbye!")
        break
    try:
        num1= float(user_input)
        op = input("Enter operator (+ , -, *, /): ").strip()
        num2 =float(input("Enter the second number:"))

            # Calculate and print the result
        result = calc(num1, op, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid numeric input! Please enter numbers only.")

        