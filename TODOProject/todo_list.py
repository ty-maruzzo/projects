def todolist():
    todolist =[]
    while True:
        
        task = input("Enter a task (or 'done' to finish): ")
        if task.lower() == "done":
            break
        todolist.append(task)
        #print(f"Task '{task}' added to the to-do list.")
        print(f"Task '{task}' added to the to-do list.")
    return todolist
tasks = todolist()
for task in tasks:
    print(f'Your task is : {task}')

