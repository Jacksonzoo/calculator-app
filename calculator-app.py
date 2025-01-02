def calculator():
    try:     
        numb1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        numb2 = float(input("Enter the second number: "))

        if operator == '+':
            ans = numb1 + numb2
        elif operator == '-':
            ans =  numb1 - numb2
        elif operator == "*" or operator == 'x':
            ans =  numb1 * numb2
        elif operator == '/':
            if numb2 == 0:
                return "Error: Cannot divide by zero."
            ans = numb1 / numb2
        else:
            return "Invalid operator. Please use +, -, *, or /."

        return f"The result is: {ans}"
    except ValueError:
        return "Invalid input. Please use numeric values"

while True:
    print(calculator())
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("Goodbye!")
        break
    


