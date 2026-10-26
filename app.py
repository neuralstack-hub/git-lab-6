
# Experiment 6: Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))

if 0 <= marks <= 100:
    grade = calculate_grade(marks)
    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
else:
    print("Please enter marks between 0 and 100.")
