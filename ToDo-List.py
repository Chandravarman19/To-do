tasks = {
    "Jogging":"Done",
    "Swimming" :"Pending",
    "Dancing" : "Done",
    "Studying" : "Done"

}

def add_task ():
    task=input("Enter a new Task to be added:")
    if task in tasks :
        tasks[task] ="Pending"
        print("Successfully Added")
    else:
        print("Not added, Try again")

def view_task():
    print(f"These are the Tasks here{tasks}")


def update_task():
    task = input("Enter a task to update:")
    if task in tasks:
       status = input("Enter  new status (Pending\Done)")
       tasks[task] = status
       print("Updated the Tasks")
    else:
        print ("Try again not done" ) 


def delete_task() :
    task = input("Enter a Task to delete it:")
    if task in tasks:
        del tasks[task]
        print("Deleted Successfully")
    else:
        print("Not deleted Yet ")

def exit_task() :
    print("Thank You and Good Byee")
    exit()


while True:
    
  print("\n 1.Add New tasks")
  print("\n 2. View tasks")
  print("\n 3.Update tasks")
  print("\n 4. Delete tasks")
  print("\n 5.Exit")




  choice = input("Enter a choice")

  if choice == "1":
      add_task()
  elif choice == "2":
      view_task()
  elif choice == "3":
      update_task()
  elif choice == "4":
      delete_task()
  elif choice == "5":
      print("Goodbye")
      break
  