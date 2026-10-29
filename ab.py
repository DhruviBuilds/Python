# Calculate and display:

# Employee name
# Basic salary
# Total allowances
# Gross salary
# Total deductions
# Net salary
# Calculation Rules
# Gross Salary = Basic Salary + Total Allowances
# Net Salary = Gross Salary - Total Deductions

# Employee_name = input("Enter employee name: ")
# basic_salary = float(input("Enter basic salary: "))
# Total_allowances = float(input("Enter total allowances: "))
# Total_deductions = float(input("Enter total deductions: "))

# print("\nSalary Details:")
# print("Employee Name: ", Employee_name)
# print("Basic Salary: ", basic_salary)
# print("Total Allowances: ", Total_allowances)
# print("Gross Salary: ", basic_salary + Total_allowances)
# print("Total Deductions: ", Total_deductions)
# print("Net Salary: ", (basic_salary + Total_allowances) - Total_deductions)

# # Task 02: Student Result Management
# Problem Statement
# Create a program that accepts a student's name and marks in five subjects.

# Calculate the total marks, percentage, and final grade.

# Grading Criteria
# Percentage	Grade
# 90% and above	A+
# 75% to below 90%	A
# 60% to below 75%	B
# 40% to below 60%	C
# Below 40%	Fail
# Assume each subject carries a maximum of 100 marks.

# Requirements
# Accept the student's name.
# Accept marks in five subjects.
# Calculate total marks out of 500.
# Calculate the percentage.
# Determine the grade using conditional statements.
# Display the student's result.

# student_name = input("\nEnter student name: ")
# subject1 = float(input("Enter marks for subject 1: "))
# subject2 = float(input("Enter marks for subject 2: "))
# subject3 = float(input("Enter marks for subject 3: "))
# subject4 = float(input("Enter marks for subject 4: "))
# subject5 = float(input("Enter marks for subject 5: "))  

# total_marks = subject1 + subject2 + subject3 + subject4 + subject5
# percentage = (total_marks / 500) * 100

# print("================Student Result==============")
# print("Student Name:",student_name)
# print("Student Marks Out Of 500:",total_marks)
# print("Student Percentage:",percentage)

# if percentage > 90:
#     print("A+")
# elif percentage >= 75 and percentage < 90:
#     print("A")
# elif percentage >= 60 and percentage <75:
#     print("B")
# elif percentage >= 40 and percentage < 60:
#     print("C")
# else:
#     print("Fail")



# Task 03: Number Analysis Tool
# Problem Statement
# Create a program that accepts an integer and analyzes the number.

# Requirements
# Determine whether the number is:

# Positive, negative, or zero.
# Even or odd.
# Divisible by 3.
# Divisible by 5.
# Divisible by both 3 and 5.

# number = int(input("\nEnter an integer: "))

# print("Positive, negative, or zero.\n")
# if number > 0:
#     print(number,"is positive")
# elif number < 0:
#     print(number,"is negative")
# else:
#     print(number,"is zero")

# print("Even or odd.\n")
# if number%2==0:
#     print("Even")
# else:
#     print("Odd")

# print("Divisivble By 3\n")
# if number%3==0:
#     print(number,"Divisible by 3")
# else:
#     print(number,"Not Divisble by 3")

# print("Divisivble By 5\n")
# if number%5==0:
#     print(number,"Divisible by 5")
# else:
#     print(number,"Not Divisble by 5")

# print("Divisible by both 3 and 5.\n")
# if number%3 ==0 and number%5==0:
#     print(number,"Divisible by 3 and 5")
# else:
#     print("Not Divisible By 3 and 5")


# Task 04: Electricity Bill Calculator
# Problem Statement
# Create a program that calculates an electricity bill based on the number of units consumed.

# Electricity Tariff
# Consumption Slab	Rate
# First 100 units	₹5 per unit
# Next 100 units	₹7 per unit
# Above 200 units	₹10 per unit
# Apply the rates progressively.

# For example, if a customer consumes 250 units:

# First 100 units: 100 × ₹5 = ₹500
# Next 100 units: 100 × ₹7 = ₹700
# Remaining 50 units: 50 × ₹10 = ₹500
# Total Bill = ₹1,700

# Requirements
# Accept the customer's name.
# Accept the total units consumed.
# Calculate the bill using the given slabs.
# Display the units consumed and the final bill.
# Reject negative unit consumption.

# customer_name = input("\nEnter customer name: ")
# units_consumed = float(input("Enter total units consumed: "))

# if units_consumed < 0:
#     print("Invalid input. Units consumed cannot be negative.")
# else:
#     if units_consumed <=100:
#         bill = units_consumed * 5
#     elif units_consumed <=200:
#         bill = (100 * 5) + ((units_consumed - 100)  * 7)
#     else:
#         bill = (100*5) + (100*7) + ((units_consumed - 200) *10)
#     print("\n==================Electricity Bill Details:")
#     print("Customer Name: ", customer_name)
#     print("Units Consumed: ", units_consumed)
#     print("Total Bill: ₹", bill)


# Task 05: Multiplication Table Generator
# Problem Statement
# Create a program that generates the multiplication table of a number entered by the user.

# Requirements
# Accept a number.
# Print its multiplication table from 1 to 10.
# Extend the program to accept a custom ending multiplier.
# Display each multiplication in a readable format.

# number = int(input("\nEnter a number to generate its multiplication table: "))
# ending_multiplier = int(input("Enter the ending multiplier: "))

# for i in range(1,ending_multiplier + 1):
#    print(f"{number} x {i} = {number * i}")