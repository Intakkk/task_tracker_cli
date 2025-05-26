import json
import sys
from datetime import datetime

def add(task_name):
    try:
        task_id = tasks[-1]["id"]+1
    except:
        task_id = 1

    task = ({"id": task_id, "name": task_name, "status": "todo", "createdAt": timestamp, "updatedAt": ""})
    tasks.append(task)

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

    return print(f"Task added successfully (ID: {task["id"]})")

def list():
    for task in tasks:
        print(f"{task['id']} {task['name']} - status: {task['status']} (created at {task['createdAt']} and updated at {task['updatedAt']})")
    return

def update(task_id, task_name):
    for task in tasks:
        if task["id"] == int(task_id):
            task["name"] = task_name
            task["updatedAt"] = timestamp

            with open("tasks.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, indent=2, ensure_ascii=False)

            return print(f"Task updated successfully (ID: {task_id})")
        else:
            return print(f"No task found (ID: {task_id})")  

try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

args = sys.argv[1:]
cmd = args[0]

globals()[cmd](*args[1:])
