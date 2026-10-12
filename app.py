import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = "comps.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            units TEXT,
            rank TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db()
    if request.method == "POST":
        conn.execute(
            "INSERT INTO comps (name, units, rank, notes) VALUES (?, ?, ?, ?)",
            (request.form["name"], request.form["units"],
             request.form["rank"], request.form["notes"]),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    comps = conn.execute("SELECT * FROM comps ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", comps=comps)

init_db()

if __name__ == "__main__":
    app.run(debug=True)