def todolist():
    todolist =[]
    while True:
        
        task = input("Enter a task (or 'done' to finish): ")
        if task.lower() == "done":
            break
        todolist.append(task)
        #print(f"Task '{task}' added to the to-do list.")
        print(f"Task '{task}' added to the to-do list.")
    return print(todolist)
todolist()
print("Your to-do list:")

