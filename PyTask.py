import pandas as pd
import numpy as np
import os.path
command = input("Enter a task to get started, \"pending\" to view pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
running = True
if os.path.isfile("Tasks.csv"):
    logfile = pd.read_csv("Tasks.csv")
    input("Enter a command to get started. (Try \"pending\", \"completed\", or \"all\")")
    if logfile.loc[logfile["Task_name"] == command].empty:
        print("The tasks list is empty. Try adding one.")
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
