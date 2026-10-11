
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if username == "admin" and password == "secret123":
        return """
        <h1>Login Successful!</h1>
        <p>Welcome, admin.</p>
        <a href="/">Back to Login</a>
        """

    return """
    <h1>Login Failed!</h1>
    <p>Incorrect username or password.</p>
    <a href="/">Try Again</a>
    """, 401


if __name__ == "__main__":
    app.run(debug=True)
