**Morse Code Web App**
A full-stack web application that allows users to **encode and decode Morse code**, with authentication, persistent history storage, and audio playback.

**🚀 Features**
1.User Authentication (Signup & Login)
2.Encode text → Morse code
3.Decode Morse code → text
4.History tracking (stored in PostgreSQL)
5.Morse audio playback
6.Interactive UI with:
  User sidebar
  History panel
  Reference (Morse chart)
7.Clean and responsive interface

**🛠️ Tech Stack**
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
Database: PostgreSQL
Libraries:
  1.psycopg2
  2.Werkzeug (password hashing)

**Project Structure**

Morse-Code-Web-App/
│
├── app.py
├── morse_logic.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   ├── auth.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── signup.html

** Setup Instructions**

1. Clone the repository
git clone https://github.com/kavinayaramesh13/Morse-Code-Web-App.git
cd Morse-Code-Web-App
2. Install dependencies
pip install -r requirements.txt
3. Setup PostgreSQL

Create database:

CREATE DATABASE morse_app;

Create tables:

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
);

CREATE TABLE history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    input_text TEXT,
    output_text TEXT,
    action TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4. Configure Database

Update your database credentials in `app.py`:

python
conn = psycopg2.connect(
    host="localhost",
    database="morse_app",
    user="postgres",
    password="your_db_password",
    port="5432"
)

5. Run the application

python app.py

6. Open in browser

http://127.0.0.1:5000

**🔊 Audio Playback**
1.Morse output is converted into audio signals
2.Supports adjustable playback speed

**Security Note**
1.Passwords are hashed using Werkzeug
2.Avoid committing real database credentials to GitHub
3.Use environment variables for production

**Future Improvements**
🌐 Deploy the app online
🎙️ Real-time communication features
🎨 UI/UX enhancements
🧠 Smart suggestions for Morse learning

Author
**Kavinaya R**

GitHub: https://github.com/kavinayaramesh13

📌 License

This project is open for learning and development purposes.
