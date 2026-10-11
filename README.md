\# Flask Login Brute-Force Lab



A beginner cybersecurity project demonstrating a local Flask login application and automated password-guessing tests using Python's `requests` library.



\## Features



\- Local Flask web server

\- HTML login form

\- Username and password validation

\- HTTP POST request handling

\- Automated dictionary-based password testing

\- HTTP response status-code analysis



\## Technologies Used



\- Python

\- Flask

\- HTML

\- Requests

\- HTTP



\## Project Structure



```text

flask-login-lab/

├── app.py

├── bruteforce.py

├── requirements.txt

├── README.md

├── .gitignore

└── templates/

&#x20;   └── login.html

```



\## Installation



Clone the repository and enter the project directory:



```bash

git clone YOUR\_REPOSITORY\_URL

cd flask-login-lab

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



\## Run the Application



Start the Flask server:



```bash

python app.py

```



Open http://127.0.0.1:5000 in your browser.



Demo credentials:



\- Username: `admin`

\- Password: `secret123`



These credentials are for local educational testing only.



\## Run the Password-Testing Script



Keep the Flask server running. Open another terminal and execute:



```bash

python bruteforce.py

```



The script submits candidate passwords from a predefined list and checks the server response.



\## Learning Objectives



\- Understand Flask routes and HTML forms

\- Learn HTTP GET and POST requests

\- Use Python loops and dictionaries

\- Automate requests using the Requests library

\- Interpret HTTP status codes

\- Understand basic password-guessing techniques



\## Security Note



This is an intentionally simple educational application. It uses hardcoded credentials and is not suitable for production.



Run the testing script only against systems you own or have explicit permission to test. Keep the application bound to localhost during practice.



\## Future Improvements



\- Add login-attempt rate limiting

\- Implement secure password hashing

\- Add Flask session management

\- Improve authentication error handling



\## Author



Md Wasif Raza



Cybersecurity learner | Python | Web Security

