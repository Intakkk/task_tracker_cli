import json
from datetime import datetime
import shlex

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

def list(task_status = None):
    for task in tasks:
        if task_status is None or task["status"] == task_status:
            print(f"{task['id']} {task['name']} - status: {task['status']} (created at {task['createdAt']} and updated at {task['updatedAt']})")
        
    return

def update(task_id, task_name):
    task = next((t for t in tasks if t["id"] == int(task_id)), None)

    if task is None:
        return print(f"No task found (ID: {task_id})") 

    task["name"] = task_name
    task["updatedAt"] = timestamp

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

    return print(f"Task name updated successfully (ID: {task_id})")

def delete(task_id):
    task = next((t for t in tasks if t["id"] == int(task_id)), None)

    if task is None:
        return print(f"No task found (ID: {task_id})") 
    
    tasks.remove(task)

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

    return print(f"Task deleted successfully (ID: {task_id})")

def mark(task_status, task_id):
    task = next((t for t in tasks if t["id"] == int(task_id)), None)

    if task is None:
        return print(f"No task found (ID: {task_id})")
    
    task["status"] = task_status
    task["updatedAt"] = timestamp

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

    return print(f"Task status updated successfully (ID: {task_id})")

while True:
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    task_cli = input("task-cli ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if task_cli.lower() in {"exit", "quit"}:
        break
    
    task_cli_split = shlex.split(task_cli)
    task_cli_resplit = task_cli_split[0].split("-", 1)
    cmd = task_cli_resplit[0]
    args = task_cli_resplit[1:] + task_cli_split[1:]

    try:
        globals()[cmd](*args)
    except KeyError:
        print(f"Unknown command : {cmd}")
    except TypeError as e:
        print(f"Wrong arguments for '{cmd}' : {e}")
