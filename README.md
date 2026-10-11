# Flask Login Brute-Force Lab

A beginner-friendly cybersecurity project demonstrating a local Flask login application and automated dictionary-based password testing using Python's `requests` library.

## Features

- Local Flask web server
- HTML login form
- Basic username and password validation
- HTTP POST request handling
- Automated password testing against a predefined list
- HTTP response status-code analysis

## Technologies Used

- Python
- Flask
- HTML and CSS
- Requests
- HTTP

## Project Structure

```text
flask-login-bruteforce-lab/
├── app.py
├── bruteforce.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── login.html
```

## Prerequisites

- Python 3 installed
- Git installed (for cloning the repository)

## Installation

Clone the repository:

```bash
git clone https://github.com/mdwasifraza01/flask-login-bruteforce-lab-.git
cd flask-login-bruteforce-lab-
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

### Demo Credentials

- **Username:** `admin`
- **Password:** `secret123`

These credentials are hardcoded for local educational testing only.

## Run the Password-Testing Script

Keep the Flask server running. Open a second terminal in the project directory and run:

```bash
python bruteforce.py
```

The script submits candidate passwords from a predefined list to the local login endpoint and checks the server's response to identify a successful login.

## Learning Objectives

- Understand Flask routes and HTML forms
- Learn HTTP GET and POST requests
- Practice Python lists, dictionaries, loops, and conditional statements
- Automate HTTP requests using the Requests library
- Interpret HTTP status codes and server responses
- Understand basic dictionary-based password guessing

## Security Disclaimer

This project is intended for educational purposes and authorized testing only.

- The application uses hardcoded credentials and is not suitable for production.
- Run the password-testing script only against your own local application or systems for which you have explicit permission.
- Keep the development server restricted to your local machine.
- Do not use real passwords or reuse the demo credentials for personal accounts.

## Future Improvements

- Add login-attempt rate limiting
- Implement secure password hashing
- Add Flask session management
- Improve authentication error handling
- Add automated unit tests

## Author

**Md Wasif Raza**

Cybersecurity Learner | Python | Web Security
