# Updated 22/1/24 (UPDATE NOT REQUIRED)

import csv
from raw_modules.whats_core import check_number
from raw_modules.calen_clock import *

# Global variable
log_path = r"H:\AI\resource_files\whatsapp_history.csv"

# Formating message that is to be sent
def format_message(message: str) -> str:
    msg_list = message.split(" ")
    new = []
    for x in msg_list:
        if "\n" in x:
            x = x.replace("\n", "")
            new.append(x) if not len(x) == 0 else None
        elif len(x) != 0:
            new.append(x)
    return " ".join(new)

# Message to be written in log for whatsapp history
def log_message(receiver: str, message: str) -> None:
    time_data=clock()
    time_data=list(time_data)
    date_data=calendar()
    date_data=list(date_data)
    message = format_message(message)
    columns = ["Day", "Month", "Year", "Hour", "Minute", "Second", "Receiver_number", "Receiver_grp_id", "Message"]
    if check_number(receiver):
        data = {
            "Day": date_data[0],
            "Month": date_data[1],
            "Year": date_data[2],
            "Hour": time_data[0],
            "Minute": time_data[1],
            "Second": time_data[2],
            "Receiver_number": receiver,
            "Message": message,
        }
    else:
        data = {
            "Day": date_data[0],
            "Month": date_data[1],
            "Year": date_data[2],
            "Hour": time_data[0],
            "Minute": time_data[1],
            "Second": time_data[2],
            "Receiver_grp_id": receiver,
            "Message": message,
        }
    try:
        with open(log_path, mode='a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# image to be written in log for whatsapp history
def log_image(path: str, receiver: str, caption: str) -> None:
    log_message(receiver,path+" : "+caption)