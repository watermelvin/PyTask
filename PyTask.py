import pandas as pd
import os.path
running = True
if os.path.isfile("Tasks.csv"):
    while running:
        # load tasks.csv as a dataframe into pandas
        tasks = pd.read_csv("Tasks.csv")
        # prompt user for a command
        command = input("Enter a task to get started, \"pending\" to view pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
        if command == "pending":
            # print out only pending tasks
            pending_tasks = tasks[tasks["Status"] == "pending"]
            print("Pending Tasks:")
            print(pending_tasks.to_string())
            # ask for which task to modify, if any
            modification = input("Enter a number of a task to change it to completed, or \"exit\" to leave this menu.")
            if modification == "exit":
                continue
            else:
                # change given task to completed
                tasks.loc[modification, "Status"] = "completed"
                tasks.to_csv("Tasks.csv", index=False)
                # after modifying, print new pending tasks list.
                print("All Tasks:")
                print(tasks.to_string())

        elif command == "completed":
            completed_tasks = tasks[tasks["Status"] == "completed"]
            print("Completed Tasks:")
            print(completed_tasks.to_string())
            # ask for which task to modify, if any
            modification = input("Enter a number of a task to change it to pending, or \"exit\" to leave this menu.")
            if modification == "exit":
                continue
            else:
                tasks.loc[modification, "Status"] = "pending"
                tasks.to_csv("Tasks.csv", index=False)
                print("All Tasks:")
                print(tasks.to_string())
        elif command == "all":
            print("All Tasks:")
            print(tasks.to_string())
            # modification = input("Enter the number of the task to modify, or \"exit\" to exit this menu.")
        elif command == "EXIT":
            running = False
        elif tasks.loc[tasks["Task Name"] == command].empty:
            print("That task isn't already in the list. Saving as a new pending task...")
            # new_pending_task = pd.DataFrame(command, "pending")
            tasks_list = open("Tasks.csv", "a")
            tasks_list.write(command + ",pending\n")
            tasks_list.close()
            tasks = pd.read_csv("Tasks.csv")
        # TODO: add a way to mark pending tasks as completed and completed as pending.
# Error in case Tasks.csv isn't there.
else:
    print("Tasks.csv not found! Attempting to make a new Tasks.csv.")
