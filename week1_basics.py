# Week 1: Python Setup, Variables, I/O, Operators, and Conditionals

print("=== Welcome to NextByte Studio Python Internship ===")

# User Input & Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Operators & Basic Calculation
current_year = 2026
birth_year = current_year - age
print(birth_year)

print(f"\nHello, {name}! You were born around {birth_year}.")

# Conditional Statements (GPA & Success Logic)
gpa = float(input("\nEnter your current GPA: "))

if gpa >= 5.00:
    print("Result: education is key to success hahaaahhaah 🔥")
elif gpa >= 3.00:
    print("Result: Good job! Keep up the consistent effort.")
else:
    print("Result: A single paper can not decide your future. Keep pushing!")