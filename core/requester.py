import requests
import json

def perform_request(preset=None):
    if not preset:
        url = input("Enter API URL: ").strip()
        method = input("HTTP Method (GET, POST, etc): ").strip().upper()
        headers = {}
        while True:
            k = input("Header key (or ENTER to skip): ").strip()
            if not k: break
            v = input(f"Value for {k}: ").strip()
            headers[k] = v
        data_input = input("Enter JSON body (or leave empty): ").strip()
        data = json.loads(data_input) if data_input else None
    else:
        url = preset["url"]
        method = preset["method"]
        headers = preset["headers"]
        data = preset["data"]

    try:
        resp = requests.request(method, url, headers=headers, json=data)
        print("\nStatus Code:", resp.status_code)
        print("Headers:", resp.headers)
        try:
            print("Response (formatted):")
            print(json.dumps(resp.json(), indent=2))
        except Exception:
            print(resp.text)
        return {
            "url": url, "method": method, "headers": headers, "data": data
        }
    except Exception as e:
        print(f"Request error: {e}")
        return None