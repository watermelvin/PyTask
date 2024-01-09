import pandas as pd
import os.path
running = True
if os.path.isfile("Tasks.csv"):
    while running:
        # load tasks.csv as a dataframe into pandas
        tasks = pd.read_csv("Tasks.csv")
        # prompt user for a command
        command = input("Enter a new task to get started, \"pending\" to view current pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
        if command == "pending":
            # print out only pending tasks
            pending_tasks = tasks[tasks["Status"] == "pending"]
            print("Pending Tasks:")
            print(pending_tasks.to_string())
            # ask for which task to modify, if any
            modification = input("Enter a number of a task to change it to completed, or \"exit\" to leave this menu.\n")
            # if no modification, exit menu.
            if modification == "exit":
                continue
            else:
                # change given task to completed
                tasks.at[int(modification), "Status"] = "completed"
                tasks.to_csv("Tasks.csv", index=False)
                # after modifying, print new pending tasks list.
                print("All Tasks:")
                print(tasks.to_string())
        elif command == "completed":
            completed_tasks = tasks[tasks["Status"] == "completed"]
            print("Completed Tasks:")
            print(completed_tasks.to_string())
            # ask for which task to modify, if any
            modification = input("Enter a number of a task to change it to pending, or \"exit\" to leave this menu.\n")
            # if no modification, exit menu.
            if modification == "exit":
                continue
            else:
                # change given task to completed
                tasks.at[int(modification), "Status"] = "pending"
                tasks.to_csv("Tasks.csv", index=False)
                # after modifying, print new pending tasks list.
                print("All Tasks:")
                print(tasks.to_string())
        elif command == "all":
            print("All Tasks:")
            print(tasks.to_string())
            modification = input("Enter the number of the task to modify, or \"exit\" to exit this menu.\n")
            # exit the menu if user inputs exit
            if modification == "exit":
                continue
            else:
                new_status = input("Enter the new status:")
                # change given task to completed
                tasks.at[int(modification), "Status"] = new_status
                tasks.to_csv("Tasks.csv", index=False)
                # message about modification
                print(f"Modified task {modification}'s status to {new_status}.")
                # after modifying, print new pending tasks list.
                print("All Tasks:")
                print(tasks.to_string())
        elif command == "exit":
            running = False
        # if the task isn't in the list already, save it as a new pending task
        elif tasks.loc[tasks["Task Name"] == command].empty:
            print("That task isn't already in the list. Saving as a new pending task...") 
            tasks_list = open("Tasks.csv", "a")
            tasks_list.write(command + ",pending\n")
            tasks_list.close()
            tasks = pd.read_csv("Tasks.csv")
        else:
            new_status = input("What modification do you want to do? (completed, pending, delete)?")
            # make this command an int, not a string.
            tasks.at[command, "Status"] = new_status
            tasks.to_csv("Tasks.csv", index=False)
            # message about modification
            print(f"Modified task {command}'s status to {new_status}.")
            # after modifying, print new pending tasks list.
            print("All Tasks:")
            print(tasks.to_string())

        # TODO: make a way to delete tasks
# Error in case Tasks.csv isn't there.
else:
    print("Tasks.csv not found! Attempting to make a new Tasks.csv.")
