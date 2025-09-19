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
    
def save_tasks(tasks): # Save tasks to file
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def views_tasks(tasks): # Display all tasks
    if not tasks:
        print("\n No tasks found!\n")
        return
    print("\n Your tasks:")
    for i, task in enumerate (tasks, start = 1):
        print(f"{i}.{task['title']}-{task['status']}")
    print()

def  add_tasks(tasks):
    title = input("Enter task title:").strip()
    if title == "":
        print("Task cannot be empty")
        returntasks.append({"title": title, "status": "Pending"})
        save_tasks(tasks)
        print("Task added successfully")

def update_tasks(tasks): #Updating the Task status
    view_tasks(tasks) 
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to update:"))
        if 1 <= choice <= len(tasks):
            tasks[choice -1]["status"] = "DONE"
            save_tasks(tasks)
            print("Updating Task is DONE")
        else:
            print("Invalis Task number") 
    except ValueError:
        print("Please enter a valid number")                                  

def delete_taks(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete"))
        if 1<= choice <= len(tasks):
            removed =tasks.pop(choice -1)
            save_tasks(tasks)
            print(f"Task'{removed['title']}' deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please Enter a valid number")

def main():
    tasks = load_tasks()
    while True:
        print("\n Task Manager\n")
        print("1.View Tasks")
        print("2.Add Tasks")
        print("3.Update Tasks")
        print("4.Delete Tasks")
        print("5. Exit")

        try:
            choice = int(input("Enter Choice"))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_tasks(tasks)
            elif choice == 3:
                update_tasks(tasks)
            elif choice == 4:
                delete_tasks(tasks)
            elif choice == 5:
                print("Exiting......Goodbye!")
                break
            else:
                print("Invalid Choice ! Please enter 1-5.")
        except ValueError:
            print("Please enter numbers only(1-5)!")

if __name__ == "__main__":
    main()

