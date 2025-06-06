import os
import json

SAVE_DIR = "saved_requests"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_request(name, data):
    with open(f"{SAVE_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Request '{name}' saved.")

def load_request(name):
    try:
        with open(f"{SAVE_DIR}/{name}.json") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Request not found.")
        return None

def list_saved_requests():
    files = os.listdir(SAVE_DIR)
    if not files:
        print("No saved requests.")
    else:
        print("Saved Requests:")
        for f in files:
            print(" -", f.replace(".json", ""))