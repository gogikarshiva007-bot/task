# Student Grade Management System

# Using Lists, Tuples and Multiple Functions
 
students = []   # Will store tuples like: (name, [marks])
 
 
# ------------------------------

# Function to add a student

# ------------------------------

def add_student():

    name = input("Enter student name: ")
 
    marks = []

    for i in range(3):

        mark = float(input(f"Enter mark {i+1}: "))

        marks.append(mark)
 
    student = (name, marks)

    students.append(student)
 
    print("Student added successfully!\n")
 
 
# ------------------------------

# Calculate average

# ------------------------------

def calculate_average(marks):

    return sum(marks) / len(marks)
 
 
# ------------------------------

# Determine grade

# ------------------------------

def calculate_grade(avg):

    if avg >= 90:

        return "A"

    elif avg >= 80:

        return "B"

    elif avg >= 70:

        return "C"

    elif avg >= 60:

        return "D"

    else:

        return "F"
 
 
# ------------------------------

# Display all students

# ------------------------------

def display_students():

    if len(students) == 0:

        print("No students available.\n")

        return
 
    print("\n--- Student Report ---")

    for student in students:

        name, marks = student

        avg = calculate_average(marks)

        grade = calculate_grade(avg)
 
        print(f"Name   : {name}")

        print(f"Marks  : {marks}")

        print(f"Average: {avg:.2f}")

        print(f"Grade  : {grade}")

        print("----------------------")
 
 
# ------------------------------

# Main Menu

# ------------------------------

def main():

    while True:

        print("\n1. Add Student")

        print("2. Display Students")

        print("3. Exit")
 
        choice = input("Enter choice: ")
 
        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            print("Exiting program...")

            break

        else:

            print("Invalid choice! Try again.")
 
 
# ------------------------------

# Run Program

# ------------------------------

main()

 