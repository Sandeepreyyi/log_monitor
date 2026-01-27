from collections import Counter
LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


# Function for count of logs
def total_log_count(logs):
    return len(logs)

# Function for counts according to levels
def count_by_level(logs):
    counter = Counter(log["level"] for log in logs)
    return dict(counter)

# Function for counts according to levels but gives 0 if any of them is having 0 count
# def count_by_level(logs):
#     counter = Counter(log["level"] for log in logs)
#     return {level: counter.get(level, 0) for level in LOG_LEVELS}


# Function for Most frequent error
def most_frequent_error(logs):
    errors = [log["message"] for log in logs if log["level"] == "ERROR"]
    if not errors:
        return None, 0
    counter = Counter(errors)

    max_count = max(counter.values())
    min_count = min(counter.values())
    messages = []
    if max_count == min_count:
        message, max_count = counter.most_common(1)[0]
        messages.append(message)
        return messages, max_count

    messages = [
        message for message, count in counter.items()
        if count == max_count
    ]
        
    return messages, max_count


# Filtering logs by the time and date range
def filter_by_time_range(logs, start, end):
    return [
        log for log in logs
        if start <= log["timestamp"] <= end
    ]
