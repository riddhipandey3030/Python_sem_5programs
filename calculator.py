# Create a calculator which is capable of performing addition,subtraction,multiplication and division
# operations on two numbers. Your program should format the output in readable manner.
#------------------------------------------------------------------------------------------
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Performing operations
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice!")