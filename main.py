import sys

from create_config_folders_files import *
from csv_log import csv_log

# will come from the config file setting
log_path = "B:\\OneDrive\\PyProjects\\Logs\\Nome_do_Processo - Projeto_Teste_Log"
process_name = "Download_Audio_Files_Teste"

# getting the current task_name
task_name = sys.argv[0]

e = ""


# noinspection PyGlobalUndefined
def main():
    global log_file_name, e
    try:
        create_csv_log_folder(log_path)
        log_file_name = create_csv_log_file(process_name)

        status = "Start_Process"
        description = "The process has started."
        csv_log(log_file_name, process_name, task_name, status, description)

        status = "Log"
        description = "Getting the input file data."
        csv_log(log_file_name, process_name, task_name, status, description)

        status = "End_Process"
        description = "The process has finished."
        csv_log(log_file_name, process_name, task_name, status, description)
    except FileNotFoundError as e:
        print(f'An error occurred in Orchestrator task:\n[{e}]')


if __name__ == '__main__':
    main()
