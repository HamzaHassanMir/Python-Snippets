# Create a calculator capable of performing addition, subtraction, 
# multiplication and division operations on two numbers. 
# Your program should format the output in a readable manner!

""" Written by hamza """

print("Enter 1st number: ")
a = float (input())
print("Enter 2nd number: ")
b = float (input())

print("Enter operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Mode")

op = input()
if op == "1":
    print("Result: ", a + b)
elif op == "2":
    print("Result: ", a - b)
elif op == "3":
    if b != 0:
        print("Result: ", a / b)
    else:
        print("Error! Division by zero is not allowed.")
elif op == "4":
    print("Result: ", a * b)
elif op == "5":
    print("Result: ", a % b)
else:
    print("Invalid operation!") 