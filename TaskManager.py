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