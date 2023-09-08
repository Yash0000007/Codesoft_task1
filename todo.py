class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Incomplete"
            print(f"{idx}. {task.title} - Due: {task.due_date} - Status: {status}")

    def mark_task_as_complete(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1].completed = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            to_do_list.add_task(task)
            print("Task added.")

        elif choice == "2":
            print("\n--- Tasks ---")
            to_do_list.view_tasks()

        elif choice == "3":
            to_do_list.view_tasks()
            task_idx = int(input("Enter the task index to mark as complete: "))
            to_do_list.mark_task_as_complete(task_idx)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
