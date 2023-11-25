import json
import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    def save_to_file(self, filename="todolist.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename="todolist.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        else:
            print(f"No file found. Starting with an empty to-do list.")

def main():
    todo_list = ToDoList()

    # Load existing tasks from file
    todo_list.load_from_file()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View To-Do List")
        print("4. Save To-Do List to File")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.save_to_file()
            print("To-Do List saved to file.")
        elif choice == "5":
            print("Quitting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
