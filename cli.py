# this is CLI file
from datetime import datetime
from analytics import (
    total_log_count,
    count_by_level,
    most_frequent_error,
    filter_by_time_range
)
from utils import export_to_json
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Options As per requirements
def show_options():
    print("\n Log Monitoring Menu")
    print("1. Total log count")
    print("2. Count per log level")
    print("3. Most frequent ERROR message")
    print("4. Filter logs by time range")
    print("5. Export analytics to JSON")
    print("6. Exit")

#choice handling switch cases
def handle_choice(choice, logs):
    if choice == "1":
        print("Total logs:", total_log_count(logs))

    elif choice == "2":
        print("Log count by level:")
        print(count_by_level(logs))

    elif choice == "3":
        error = most_frequent_error(logs)
        print("Most frequent ERROR:", error or "No ERROR logs")


    elif choice == "4":
        try:
            start = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
            end = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")

            if not start or not end:
                print("Start and end times cannot be empty.")
                return True
            if start >= end:
                print("Start time must be before end time.")
                return True
            start_dt = datetime.strptime(start, DATE_FORMAT)
            end_dt = datetime.strptime(end, DATE_FORMAT)

            filtered = filter_by_time_range(logs, start_dt, end_dt)

            if not filtered:
                print("No logs in this time range.")
            else:
                for log in filtered:
                    print(
                        f'{log["timestamp"]} {log["level"]} {log["message"]}'
                    )
        except ValueError:
            print("Invalid date format.")


    elif choice == "5":
        report = {
            "total_logs": total_log_count(logs),
            "count_by_level": count_by_level(logs),
            "most_frequent_error": {
            "message": most_frequent_error(logs)[0],
            "count": most_frequent_error(logs)[1]
        }
        }
        export_to_json(report)

    elif choice == "6":
        print("Exit")
        return False

    else:
        print("Invalid choice")

    return True
