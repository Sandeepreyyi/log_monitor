# This is main file for run the all files
from log_reader import read_logs
from cli import show_options, handle_choice

def main():
    logs = read_logs("sample.log")
    if not logs:
        print("No logs are there")
        return

    running = True
    while running:
        show_options()
        choice = input("Enter choice: ")
        running = handle_choice(choice, logs)

if __name__ == "__main__":
    main()
