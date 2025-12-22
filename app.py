from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(__name__)

# ❌ Hardcoded secret (Sonar: Security Hotspot)
API_KEY = "hardcoded_secret_123"

@app.route("/")
def home():
    return "Vulnerable Flask App for SonarQube"

@app.route("/login", methods=["POST"])
def login():
    # ❌ SQL Injection
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)

    return "Login attempted"

@app.route("/cmd")
def run_cmd():
    # ❌ Command Injection
    cmd = request.args.get("cmd")
    return subprocess.getoutput(cmd)

@app.route("/read")
def read_file():
    # ❌ Path Traversal
    file = request.args.get("file")
    with open(file, "r") as f:
        return f.read()

@app.route("/env")
def env():
    # ❌ Sensitive information exposure
    return str(os.environ)

if __name__ == "__main__":
    # ❌ Debug mode enabled
    app.run(debug=True)
