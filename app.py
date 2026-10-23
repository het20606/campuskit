from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Sample records so the app is useful as soon as it starts.
materials = [
    {"id": 1, "subject": "Cloud Computing", "title": "CCD Unit 3 notes", "kind": "Notes", "status": "To review"},
    {"id": 2, "subject": "Software Engineering", "title": "Function point examples", "kind": "Practice", "status": "In progress"},
    {"id": 3, "subject": "Computer Networks", "title": "TCP vs UDP comparison", "kind": "Revision", "status": "Done"},
]
next_id = 4


@app.route("/")
def home():
    return render_template("index.html", materials=materials)


@app.route("/add", methods=["POST"])
def add_material():
    global next_id
    subject = request.form.get("subject", "").strip()
    title = request.form.get("title", "").strip()
    kind = request.form.get("kind", "Notes").strip()
    if subject and title:
        materials.append({
            "id": next_id,
            "subject": subject,
            "title": title,
            "kind": kind or "Notes",
            "status": "To review",
        })
        next_id += 1
    return redirect(url_for("home"))


@app.route("/status/<int:item_id>", methods=["POST"])
def update_status(item_id):
    for item in materials:
        if item["id"] == item_id:
            order = ["To review", "In progress", "Done"]
            item["status"] = order[(order.index(item["status"]) + 1) % len(order)]
            break
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
