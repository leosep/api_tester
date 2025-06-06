# API Tester Pro

**API Tester Pro** is a simple command-line tool that lets you interact with APIs. It allows you to send HTTP requests, save them for later reuse, and inspect responses, all through an interactive CLI menu.

---

## Features

- Send `GET`, `POST`, `PUT`, `DELETE`, `PATCH` requests
- Add custom headers and JSON body
- Save API requests with custom names
- Reuse and run saved requests
- Pretty-print JSON responses
- Organized codebase and test structure

---

## Installation

1. **Clone the repository or extract the ZIP:**

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## How to Use

### Run the app:

```bash
python main.py
```

### Menu Options:

```
=== API Tester Pro ===
1. Make a new API request
2. List saved requests
3. Run saved request
0. Exit
```

---

## Making an API Request

- Enter the API URL.
- Choose HTTP method: GET, POST, etc.
- Add headers as key-value pairs (press ENTER to finish).
- Enter JSON request body (if any).
- Response will be printed with status code, headers, and JSON-formatted content.

---

## Saving and Reusing Requests

- After a request, you can **save it by name** (e.g., "get_users").
- You can list all saved requests.
- Run any saved request again later.

Saved requests are stored in `saved_requests/` as `.json` files.

---

## Project Structure

```
api_tester_pro/
├── main.py
├── core/
│   ├── menu.py              # CLI interaction logic
│   └── requester.py         # HTTP request logic
├── storage/
│   └── manager.py           # Saving and loading requests
├── saved_requests/          # Saved request JSON files
├── tests/
│   └── test_basic.py        # Sample test case
└── requirements.txt         # Dependencies
```

---

## Testing

Run basic tests using:

```bash
python -m unittest discover tests
```

---

## Requirements

- Python 3.7+
- `requests` library

Install with:

```bash
pip install -r requirements.txt
```

---

## License

MIT License. Feel free to modify, improve, and share!

---

## Contributing

Pull requests are welcome. For feature requests or bugs, open an issue or submit a PR.

---

## Author

Built by Leandro Sepulveda for simplicity in API testing.