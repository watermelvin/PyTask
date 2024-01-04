import pandas as pd
import os.path
running = True
if os.path.isfile("Tasks.csv"):
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
        exit
    elif tasks.loc[tasks["Task Name"] == command].empty:
        print("That task isn't already in the list. Saving as a new pending task...")

# Error in case Tasks.csv isn't there.
else:
    print("Tasks.csv not found!")
# tasks = {}
# running = True
# while running is True:
#     command = input("Enter a task to get started, \"pending\" to view pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
#     if command == "pending":
#         print('''all the pending tasks using dictionary stuff''')
#         print("Pending Tasks:")
#         for task, status in tasks.items():
#             if status == "pending":
#                 print(f"{task}")
#         # if a user enters a task that is already in the pending list, change it to completed.
#         task_in_question = input("Enter the name of a pending task to mark it as complete.")
#         if task_in_question in tasks.items():
#             tasks.pop(task_in_question)
#     # if a user enters "completed" print completed tasks.
#     elif command == "completed":
#         print("Completed Tasks:")
#         for items, status in tasks:
#             if status == "completed":
#                 print({items}, {status})
#         # if a user writes a task that is already in the completed list, change it to pending.
#     # if a user enters EXIT, exit the program.
#     elif command == "EXIT":
#         running = False
#     # if a user enters all, print all tasks.
#     elif command == "all":
#         print("All Tasks:")
#         for task, status in tasks.items():
#             print(f"[] {task}, {status}")
#     #if a user enters anything but the specified commands, save it as a pending task.
#     else:
#         print("saving the new task as pending")
#         tasks[command] = 'pending'
