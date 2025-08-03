first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Choose an operation (+, -, *, /): ")

if operator == "+":
    answer = first_number + second_number
    print(f"{first_number} + {second_number} = {answer}")
elif operator == "-":
    answer = first_number - second_number
    print(f"{first_number} - {second_number} = {answer}")
elif operator == "*":
    answer = first_number * second_number
    print(f"{first_number} * {second_number} = {answer}")
elif operator == "/":
    if second_number == 0:
        print("You can't divide by zero.")
    else:
        answer = first_number / second_number
        print(f"{first_number} / {second_number} = {answer}")
else:
    print("Sorry, that operation is not supported.")

