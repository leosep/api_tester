from core.requester import perform_request
from storage.manager import save_request, load_request, list_saved_requests

def main_menu():
    while True:
        print("\n=== API Tester Pro ===")
        print("1. Make a new API request")
        print("2. List saved requests")
        print("3. Run saved request")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            req = perform_request()
            if req:
                save = input("Save this request? (y/n): ").strip().lower()
                if save == 'y':
                    name = input("Enter a name for this request: ").strip()
                    save_request(name, req)
        elif choice == "2":
            list_saved_requests()
        elif choice == "3":
            name = input("Enter the request name: ").strip()
            req = load_request(name)
            if req:
                perform_request(preset=req)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")