import json 
FILENAME = "task.json"

def load_tasks(): #Load tasks from file
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError: #If file does not exist, return empty list
        return[]
    except json.JSONDecodeError: #If file is corrupted?empty, return empty list.
        return[]
    
def save_tasks(): # Save tasks to file
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def views_tasks(): # Display all tasks
    if not tasks:
        print("\n No tasks found!\n")
        return
    print("\n Your tasks:")
    for i, task in enumerate (tasks, start = 1):
        print(f"{i}.{task['title']}-{task['status']}")
    print()