import csv
import os
from datetime import datetime


def csv_log(file_name, process_name, task_name, status, description):
    try:
        created_at = datetime.now()
        logged_user = os.getlogin()

        process_name = process_name.lstrip()
        process_name = process_name.rstrip()
        process_name = process_name.strip()

        if "/" in task_name:
            task_name = task_name[task_name.rindex('/') + 1:]
            task_name = task_name.lstrip()
            task_name = task_name.rstrip()
            task_name = task_name.strip()
        elif "\\" in task_name:
            task_name = task_name[task_name.rindex('\\') + 1:]
            task_name = task_name.lstrip()
            task_name = task_name.rstrip()
            task_name = task_name.strip()

        status = status.lstrip()
        status = status.rstrip()
        status = status.strip()

        description = description.lstrip()
        description = description.rstrip()
        description = description.strip()

        # "Created_At", "Process_Name", "Task_Name", "User_Name", "Status", "Description"
        data = [str(created_at), str(process_name), str(task_name), str(logged_user), str(status), str(description)]

        print(data)

        with (open(file_name, 'a') as file):
            writer = csv.writer(file, delimiter = ',', lineterminator = '\n', )
            writer.writerow(data)
        file.close()

    except FileNotFoundError as e:
        print(f'An error occurred while creating the log file:\n[{e}]')
