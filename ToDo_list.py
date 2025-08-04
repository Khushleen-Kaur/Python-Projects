#TODO list

from datetime import date
print(date.today())
tasks = []
def AddTask():
    task_name = input("Enter task name : ")
    tasks.append({"task": task_name, "done": False})
    print("Task added.\n")

def DelTask():
    ViewTask()
    try:
        index = int(input("Enter index of task you want to delete : ")) - 1
        if( 0 <= index < len(tasks) ):
            removed = tasks.pop(index)
            print(f"Deleted task : {removed['tasks']}\n")
        else:
            print("Invalid task number. Try again.")

    except ValueError:
        print("Please enter a vaild number.\n")

def MarkStatus():
    ViewTask()
    try:
        index=int(input("Enter index of task status to change : "))-1
        if(0<index<len(tasks)):
            tasks[index]["done"]= not tasks[index]["done"]
            status = "completed" if tasks[index]['done'] else "incomplete"
            print(f"Marked as {status}:{tasks[index]['task']}.")
        else:
            print("Invalid Task number.")
    except ValueError:
        print("Please eter a valid number.\n")

def ViewTask():
    if not tasks:
        print("There are no tasks yet.")
    else:
        print("____TODO LIST____")
        for i,task in enumerate(tasks,1):
            status = "completed" if task['done'] else "incomplete"
            print(f"{i}.[{status}] {task['task']}")

def main():
    while True:
        print("__MAIN MENU__") 
        print("1.Add Task\n2.Del Task\n3.View Tasks\n4.Mark Complete/Incomplete\n5.Exit")
        choice = int(input("Enter Your choise number(1-5) : "))
        if(choice == 1):
            AddTask()
        elif(choice == 2):
            DelTask()
        elif choice == 3 : 
            ViewTask()
        elif choice == 4 :
            MarkStatus()
        elif choice == 5 :
            print("GoodBye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
        