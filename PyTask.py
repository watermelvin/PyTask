tasks = {}
running = True
while running is True:
    command = input("Enter a task to get started, \"pending\" to view pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
    if command == "pending":
        print('''all the pending tasks using dictionary stuff''')
        print("Pending Tasks:")
        for task, status in tasks.items():
            if status == "pending": 
                print(f"{task}")
    # if a user enters "completed" print completed tasks.
    elif command == "completed":
        print("Completed Tasks:") 
        for items, status in tasks:
            if status == "completed":
                print({items}, {status})
    # if a user enters EXIT, exit the program.
    elif command == "EXIT":
        running = False
    # if a user enters all, print all tasks.
    elif command == "all":
        print("All Tasks:")  
        for task, status in tasks.items():
            print(f"[] {task}, {status}")
    #if a user enters anything but the specified commands, save it as a pending task.
    else:
        print("saving the new task as pending")
        tasks[command] = 'pending'
