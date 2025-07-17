# Simple Command-Line To-Do List in Python

todo_list = []

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. ➕ Add Task")
    print("2. ❌ Remove Task")
    print("3. 📋 View Tasks")
    print("4. 🚪 Exit")
    print("================================")

def add_task():
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"✅ '{task}' added to your to-do list!")

def remove_task():
    if not todo_list:
        print("⚠️  No tasks to remove.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"❌ '{removed_task}' has been removed.")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def view_tasks():
    if not todo_list:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("👋 Thank you! Exiting To-Do List App. Bye OG!")
        break
    else:
        print("❗ Invalid choice. Please try again.")