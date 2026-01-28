def get_students():
    students = {}
    while True:
        name = input("Enter student name (or 'stop'): ")
        if name.lower() == "stop":
            break
        score = int(input("Enter score: "))
        students[name] = score
    return students

def calculate_average(students):
    total = sum(students.values())
    return total / len(students)

def display_results(students):
    for name, score in students.items():
        print(name, ":", score)

students = get_students()
display_results(students)
average = calculate_average(students)

print("Average Score:", average)
