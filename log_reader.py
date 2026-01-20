# This file is Log reader o read log data in file
from datetime import datetime
import re


LOG_PATTERN = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(INFO|WARNING|ERROR)\] (.*)"

# Function for checking regular experssion
def parse_log_line(line):
    match = re.match(LOG_PATTERN, line)
    if not match:
        return None

    date, time, level, message = match.groups()
    timestamp = datetime.strptime(
        f"{date} {time}", "%Y-%m-%d %H:%M:%S"
    )

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


# Function for reading file Line by line
def read_logs(file):
    logs = []
    try:
        with open(file, "r") as file:
            for line in file:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"Error reading logs: {e}")

    return logs
