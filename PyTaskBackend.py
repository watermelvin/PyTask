import pandas as pd
import os.path

# check if there's a Tasks.csv present
def check_for_Tasks():
    if os.path.isfile("Tasks.csv"):
        return True
    else:
        return False
# load tasks.csv as a dataframe into pandas
def update_tasks_dataframe(): 
    tasks = pd.read_csv("Tasks.csv")
# the main user prompt
#def main_menu_prompt():
#    command = input("Enter a new task to get started, \"pending\" to view current pending tasks, \"completed\" for completed items, or \"all\" for all items and their status. \n")
#    if command == "pending":
#        return_pending_tasks()
#    elif command == "completed":
#        return_completed_tasks()
#    elif command == "all":
#        return_all_tasks()

def return_pending_tasks():
    update_tasks_dataframe()
    pending_tasks = tasks[tasks["Status"] == "pending"]
    return pending_tasks

def return_completed_tasks():
    update_tasks_dataframe()
    completed_tasks = tasks[tasks["Status"] == "completed"]
    return completed_tasks

def return_all_tasks():
    update_tasks_dataframe()
    return tasks 

def locate_task_by_name(task_to_find):
    matching_row = tasks[task_to_find] == task_to_find
    return matching_row

def modify_task(task_to_modify, new_status):
    tasks.loc[locate_task_by_name(task_to_modify), "Status"] = new_status
    
