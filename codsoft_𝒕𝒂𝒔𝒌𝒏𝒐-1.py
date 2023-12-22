tasks = []
def Dispaly_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")
def del_task():
    Dispaly_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(tasks):
                del tasks[index - 1]
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to delete.")
def Task1codsoft():
    while True:
        print("\n Welcome To  To-Do List Opeations Have a Nice Day!!")
        print("Menu List:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your Task: ")

        if choice == "1":
            Dispaly_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            del_task()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

Task1codsoft()
