tasks = {}
habits = {}

def add_task():
    task = input("Enter task: ")
    tasks[task] = False

def complete_task():
    task = input("Enter task to mark done: ")
    if task in tasks:
        tasks[task] = True

def add_habit():
    habit = input("Enter habit: ")
    habits[habit] = 0

def complete_habit():
    habit = input("Habit completed today: ")
    if habit in habits:
        habits[habit] += 1

def wellness_insight():
    completed = sum(tasks.values())
    print("Tasks completed:", completed)
    for habit, streak in habits.items():
        print(f"{habit} streak: {streak}")
    if completed > 0:
        print("Great job! You're making progress 🌟")
    else:
        print("Try completing at least one task today 💪")

while True:
    print("\n1.Add Task 2.Complete Task 3.Add Habit 4.Complete Habit 5.Insight 6.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        add_habit()
    elif choice == "4":
        complete_habit()
    elif choice == "5":
        wellness_insight()
    elif choice == "6":
        break
