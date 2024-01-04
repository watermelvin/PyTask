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
        elif command == "completed":
            completed_tasks = tasks[tasks["Status"] == "completed"]
            print("Completed Tasks:")
            print(completed_tasks.to_string())
        elif command == "all":
            print("All Tasks:")
            print(tasks.to_string())
        elif command == "EXIT":
            running = False
        elif tasks.loc[tasks["Task Name"] == command].empty:
            print("That task isn't already in the list. Saving as a new pending task...")
            # new_pending_task = pd.DataFrame(command, "pending")
            tasks_list = open("Tasks.csv", "a")
            tasks_list.write(command + ",pending\n")

# Error in case Tasks.csv isn't there.
else:
    print("Tasks.csv not found!")
