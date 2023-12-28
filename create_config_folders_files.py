import csv
import os
from datetime import datetime, date

current_log_path = ""
current_log_file = ""


def create_csv_log_folder(path):
    global current_log_path
    try:
        today = datetime.today()
        current_year = str(today.year)
        current_month = str(today.month)
        current_day = str(today.day)
        current_log_path = path + "/" + current_year + "/" + current_month + "/" + current_day

        if not os.path.exists(current_log_path):
            os.makedirs(current_log_path)

    except Exception as e:
        print(f'An error occurred while creating the log folder [{current_log_path}]:\n[{e}]')


def create_csv_log_file(file):
    global current_log_file
    try:
        current_day = str(date.today())
        current_log_file = current_log_path + "/" + file + "_" + current_day + ".csv"

        if not os.path.isfile(current_log_file):
            header = ["Created_At", "Process_Name", "Task_Name", "User_Name", "Status", "Description"]

            with (open(current_log_file, 'w') as file):
                writer = csv.writer(file, delimiter = ',', lineterminator = '\n', )
                writer.writerow(header)
            file.close()

        return current_log_file

    except FileNotFoundError as e:
        print(f'An error occurred while creating the log file[{current_log_file}]:\n[{e}]')
