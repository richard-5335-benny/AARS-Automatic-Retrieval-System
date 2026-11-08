from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "aars-development-key"

# Temporary prototype data
users = {}
items = [
    {"id": 1, "name": "DC Motor", "location": "Rack B-07", "stock": 8, "icon": "⚙"},
    {"id": 2, "name": "Motor Driver", "location": "Rack A-12", "stock": 4, "icon": "▣"},
    {"id": 3, "name": "Ultrasonic Sensor", "location": "Rack C-03", "stock": 15, "icon": "◉"},
    {"id": 4, "name": "Raspberry Pi", "location": "Rack D-02", "stock": 6, "icon": "⌁"},
]

requests_db = []


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if email in users:
            return render_template(
                "register.html",
                error="An account with this email already exists."
            )

        users[email] = {
            "name": name,
            "password": password
        }

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = users.get(email)

        if user and user["password"] == password:
            session["user"] = email
            session["name"] = user["name"]
            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Incorrect email or password."
        )

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    active = len([
        r for r in requests_db
        if r["status"] != "Completed"
    ])

    completed = len([
        r for r in requests_db
        if r["status"] == "Completed"
    ])

    return render_template(
        "dashboard.html",
        name=session["name"],
        items=items,
        active=active,
        completed=completed
    )


@app.route("/request/<int:item_id>", methods=["GET", "POST"])
def request_item(item_id):
    if "user" not in session:
        return redirect(url_for("login"))

    item = next((x for x in items if x["id"] == item_id), None)

    if not item:
        return "Item not found", 404

    if request.method == "POST":
        quantity = int(request.form["quantity"])
        priority = request.form["priority"]

        request_id = f"AARS-{len(requests_db) + 2401}"

        new_request = {
            "id": request_id,
            "item": item["name"],
            "location": item["location"],
            "quantity": quantity,
            "priority": priority,
            "status": "Searching"
        }

        requests_db.append(new_request)

        return redirect(
            url_for("status", request_id=request_id)
        )

    return render_template(
        "request.html",
        item=item
    )


@app.route("/status/<request_id>")
def status(request_id):
    if "user" not in session:
        return redirect(url_for("login"))

    req = next(
        (r for r in requests_db if r["id"] == request_id),
        None
    )

    if not req:
        return "Request not found", 404

    return render_template(
        "status.html",
        req=req
    )


if __name__ == "__main__":
    app.run(debug=True)