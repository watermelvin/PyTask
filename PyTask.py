tasks = {}
running = True
while running == True:
    command = input("Enter a task to get started, \"pending\" to view a list of all pending tasks, \"completed\" for completed items.\n")
    if command == "pending":
        print('''all the pending tasks using dictionary stuff''')
    elif command == "completed":
        print('''all the completed tasks using dictionary stuff''')
        for items in tasks:
            if value in tasks.values() == completed:
                print(item)
# if a user inputs something other than pending or completed, save it as a pending task.
    elif command == "EXIT":
        running = False
    else:
        print('''saving the new task as pending''')
# if a user enters EXIT, exit the program.
