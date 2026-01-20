import json

def export_to_json(data, filename="report.json"):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4, default=str)
        print(f"Report exported to {filename}")
    except Exception as e:
        print(f" Failed to export JSON: {e}")
