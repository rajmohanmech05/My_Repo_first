#calculator program to perform arithmetic operation
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operator = input("Enter operator (+,-,*,/) :")

if operator == "+":
    result = num1 + num2
    print("result =", result)
elif operator == "-":
    result = num1 - num2
    print("Result =", result)
elif operator == "*" :
    result = num1 * num2
    print("Result =", result)
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else :
        result = num1 / num2
        print("Result =", result)
else:
    print("Error: Invalid Operator.")
    result = None

# Check if result is positive, Negative, or Zero
if result is not None:
    if result > 0:
        print ("Positive")
    elif    result < 0:
        print ("Negative")
    else:
        print ("Zero")

# Student grade calculator
name = input("Student Name: ")

subject1 = float(input("Enter the subject 1 mark (0-100)"))
subject2 = float(input("Enter the subject 2 mark (0-100)"))
subject3 = float(input("Enter the subject 3 mark (0-100)"))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"

elif percentage >= 60: 
    grade = "B"

elif percentage >= 40 : 
    garde = "C"

else:
    grade = "F"

# print result
print("\nStudent Name:", name)
print("Total:", total, "/300")
print("percentage:", percentage, "%")
print("Grade:", grade)
