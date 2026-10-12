from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

comps = []  # temporary storage, resets when the server stops

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        comps.append({
            "name": request.form["name"],
            "units": request.form["units"],
            "notes": request.form["notes"],
        })
        return redirect(url_for("home"))
    return render_template("index.html", comps=comps)

if __name__ == "__main__":
    app.run(debug=True)