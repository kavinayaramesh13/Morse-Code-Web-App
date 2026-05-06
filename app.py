from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from morse_logic import encode_text, decode_text

app = Flask(__name__)
app.secret_key = "morse_secret_key"

conn = psycopg2.connect(
    host="localhost",
    database="morse_app",
    user="postgres",
    password="kavihiy13",
    port="5432"
)

# HOME
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("morse"))
    return redirect(url_for("login"))

# SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        hashed_password = generate_password_hash(password)
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)",
                (username, email, hashed_password)
            )
            conn.commit()
            cur.close()
            return redirect(url_for("login"))

        except psycopg2.Error:
            conn.rollback()
            message = "Username or Email already exists."

        cur.close()

    return render_template("signup.html", message=message)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        cur = conn.cursor()
        cur.execute(
            "SELECT id, username, email, password FROM users WHERE username=%s",
            (username,)
        )

        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[3], password):
            session.clear()
            session["user_id"] = user[0]
            session["username"] = user[1]
            session["email"] = user[2]

            return redirect(url_for("morse"))
        else:
            message = "Invalid username or password."

    return render_template("login.html", message=message)

# MORSE APP (POSTGRESQL HISTORY)
@app.route("/morse", methods=["GET", "POST"])
def morse():
    if "user_id" not in session:
        return redirect(url_for("login"))

    output = ""
    user_id = session["user_id"]

    cur = conn.cursor()

    if request.method == "POST":
        text = request.form["text"]
        action = request.form["action"]

        if not text.strip():
            output = "Please enter something"
        else:
            if action == "encode":
                output = encode_text(text)
            else:
                output = decode_text(text)

            # SAVE TO DATABASE
            cur.execute(
                "INSERT INTO history (user_id, input_text, output_text, action) VALUES (%s,%s,%s,%s)",
                (user_id, text, output, action)
            )
            conn.commit()

    # FETCH HISTORY
    cur.execute(
        "SELECT input_text, output_text, action FROM history WHERE user_id=%s ORDER BY id DESC LIMIT 10",
        (user_id,)
    )

    rows = cur.fetchall()
    cur.close()

    history = []
    for r in rows:
        if r[2] == "encode":
            history.append(f"Text: {r[0]} → Morse: {r[1]}")
        else:
            history.append(f"Morse: {r[0]} → Text: {r[1]}")

    return render_template(
        "index.html",
        output=output,
        username=session.get("username"),
        email=session.get("email"),
        history=history
    )

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)