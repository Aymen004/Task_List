# Python To-Do List

This is a simple command-line To-Do List application written in Python.

## Features

- Add tasks to the to-do list.
- Mark tasks as completed.
- View all tasks along with their status (completed or not).
- Save the to-do list to a file.
- Load the to-do list from a file.

## Code Overview

The application is contained in a single Python file, `todolist.py`. Here's a brief overview of what each part of the code does:

- The `ToDoList` class represents a to-do list. It has methods to add tasks, mark tasks as completed, view all tasks, save the to-do list to a file, and load the to-do list from a file.
- The `main` function is the main loop of the application. It creates a `ToDoList` object, loads any existing tasks from a file, and then enters a loop where it displays a menu of options to the user and performs the chosen action.
- The `if __name__ == "__main__":` line at the end of the file ensures that the `main` function is only called when the file is run directly, not when it is imported as a module.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

