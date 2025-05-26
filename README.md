# 📝 Task CLI
A simple Python command-line interface (CLI) tool for managing a to-do list. Tasks are stored in a local `tasks.json` file and can be added, listed, updated, marked with a status, or deleted.

## 📦 Features
- Add new tasks with a name
- List all tasks or filter by status (`todo`, `done`, `in-progress`)
- Update the name of a task
- Mark a task with a new status
- Delete tasks by ID
- All tasks are saved persistently in a `tasks.json` file

## 🚀 Getting Started
### Requirements:
- Python 3.7+

### Installation
1. Clone this repository or copy the script into a `.py` file.
2. Run it using:
```
python task_cli.py
```

## 💡 Usage
Once the script is running, you'll be prompted with `task-cli`, where you can enter commands:

### Add a task
```
add "Buy groceries"
```

### List all tasks
```
list
```

### List tasks by status
```
list todo
list done
list in-progress
```

### Update a task's name
```
update 3 "Buy groceries and cook dinner"
```
(Here, 3 is the task ID)

### Mark a task as done/in-progress/todo
```
mark-done 2
```
(Changes task with ID 2 to done)

### Delete a task
```
delete 1
```
(Deletes task with ID 1)

### Exit the CLI
```
exit
```
or
```
quit
```

## 📂 Data Persistence
Tasks are stored in a local file called `tasks.json`.

Each task includes:
- `id`: Unique integer identifier
- `name`: Task description
- `status`: `todo`, `done`, or `in-progress`
- `createdAt`: Timestamp of creation
- `updatedAt`: Timestamp of last update (if any)

## ⚠️ Notes
Task IDs are automatically incremented.
The tool gracefully handles invalid inputs and provides error messages for:
- Invalid status values
- Non-integer task IDs
- Missing arguments
- Unknown commands

## 📄 License
This project is free to use and modify. No license specified.
