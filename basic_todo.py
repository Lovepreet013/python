tasks = []

def show_menu():
    print("\n==== To-Do List Menu ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit\n")
    
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            if(task["done"]):
                print(f'{i + 1}. {task["title"]} - Done')
            else : 
                print(f'{i + 1}. {task["title"]} - Not Done')

def add_task():
    title = input("Enter task title: ")
    tasks.append({'title': title, 'done': False})
    print("Task added successfully.")

def mark_done():
    view_tasks()
    try : 
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            print("Task marked as done!")
        else : 
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

#Main loop
while True:
    show_menu()
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice =="2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")