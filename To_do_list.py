import time
print("--- To-Do List Menu ---\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
choice=int(input("Enter your choice"))
task=[]
def choose(choice, task):
    if choice == 1:
        f=open("To_Do.txt", "a")
        new=input("Enter your task")
        task.append(new)
        f.write(new+"\n")
        f.close()
    elif choice == 2:
        f=open("To_Do.txt")
        print(f.read())
        f.close()
    elif (choice == 3):
        delete=int(input("Which task do you want to remove"))
        task.pop(delete)
        f=open("To_Do.txt","w")
        for i in task:
            f.write(i)
        f.close()
        print("The selected task has been removed")
    elif choice == 4:
        print("You have exited successfully!")
    else:
        print("Invalid")

    time.sleep(2)
    again=input("Do you want to access this again? (yes/no)")
    if again.lower()=="yes":
        choice=int(input("\nEnter your choice"))
        choose(choice, task)
    else:
        print("You have exited successfully")

choose(choice, task)
